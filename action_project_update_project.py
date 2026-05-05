from __future__ import annotations

import sys
import argparse
from pathlib import Path
import shutil
import fnmatch
import yaml
from typing import Any, Dict, List, Tuple

# --- CONFIGURABLE PATHS ---
DEFAULT_CONFIG_PATH = Path(r"C:\od\OneDrive\docs\oomp_base\webserver\config_part_source.yaml")
PROJECT_BASE_PATH = Path(r"C:\gh\project_base")

# --- FILES/FOLDERS TO COPY ---
# Edit this dict to add/remove files/folders or exclusions
PROJECT_UPDATE_ITEMS = {
    "scad_help.py": {
        "type": "file",
        "always_include": True,
    },
    
    "action_*.bat": {
        "type": "file",
        "always_include": True,
    },
    "source_file": {
        "type": "folder",
        "exclude": [],
        "always_include": True,
    },
    "webserver": {
        "type": "folder",
        "exclude": [
            "config_*.yaml",
        ],
        "always_include": True,
    },
}

# --- UTILITY FUNCTIONS ---
def load_directories(config_path: Path) -> List[Path]:
    with config_path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle) or {}
    directories = config.get("directories", [])
    if not isinstance(directories, list):
        raise ValueError("Expected 'directories' to be a list in config_part_source.yaml")
    base_dir = config_path.parent.parent
    normalized = []
    for directory in directories:
        if not isinstance(directory, str):
            continue
        cleaned = directory.strip()
        if cleaned:
            resolved = Path(cleaned)
            # Ignore relative paths
            if not resolved.is_absolute():
                continue
            normalized.append(resolved)
    return normalized

def match_exclude_patterns(name: str, patterns: List[str]) -> bool:
    for pat in patterns:
        if fnmatch.fnmatch(name, pat):
            return True
    return False

def collect_folder_files(src_folder: Path) -> List[Tuple[Path, Path]]:
    """Return list of (src, rel_path) for all files in src_folder (no exclusions here)."""
    file_list = []
    for path in src_folder.rglob("*"):
        rel = path.relative_to(src_folder)
        if path.is_file():
            file_list.append((path, rel))
    return file_list

def collect_file_matches(pattern: str) -> List[Path]:
    """Return all files in the project base matching a literal name or glob pattern."""
    return sorted(
        [path for path in PROJECT_BASE_PATH.glob(pattern) if path.is_file()],
        key=lambda path: str(path).lower(),
    )

def summarize_actions(actions: List[Tuple[Path, List[Dict[str, Any]]]], max_items: int = 5) -> str:
    lines = []
    projects_with_changes = 0
    total_new = 0
    total_updated = 0

    for target_dir, acts in actions:
        if not acts:
            continue

        projects_with_changes += 1
        new_count = sum(1 for item in acts if item["change_type"] == "new")
        updated_count = sum(1 for item in acts if item["change_type"] == "updated")
        total_new += new_count
        total_updated += updated_count

        lines.append(
            f"Target: {target_dir} ({len(acts)} files: {new_count} new, {updated_count} updated)"
        )

        for item in acts[:max_items]:
            lines.append(f"  {item['change_type']}: {item['dst']}")

        if len(acts) > max_items:
            lines.append(f"  ...and {len(acts) - max_items} more")

    total_changes = total_new + total_updated
    header = (
        f"Projects with changes: {projects_with_changes}\n"
        f"Total file changes: {total_changes} ({total_new} new, {total_updated} updated)"
    )

    if lines:
        return header + "\n\n" + "\n".join(lines)
    return header

import hashlib

def files_are_different(src: Path, dst: Path) -> bool:
    """Return True if dst does not exist or contents differ from src."""
    if not dst.exists():
        return True
    try:
        if src.stat().st_size != dst.stat().st_size:
            return True
        # Compare content in chunks
        with src.open('rb') as fsrc, dst.open('rb') as fdst:
            while True:
                bsrc = fsrc.read(8192)
                bdst = fdst.read(8192)
                if bsrc != bdst:
                    return True
                if not bsrc:
                    break
        return False
    except Exception:
        return True  # If error, assume different

def build_copy_actions(target_dirs: List[Path]) -> List[Tuple[Path, List[Dict[str, Any]]]]:
    all_actions = []
    for target_dir in target_dirs:
        actions = []
        for name, opts in PROJECT_UPDATE_ITEMS.items():
            dst = target_dir / name
            if opts["type"] == "file":
                for src in collect_file_matches(name):
                    dst = target_dir / src.name
                    if files_are_different(src, dst):
                        actions.append(
                            {
                                "type": "file",
                                "src": src,
                                "dst": dst,
                                "change_type": "new" if not dst.exists() else "updated",
                            }
                        )
            elif opts["type"] == "folder":
                src = PROJECT_BASE_PATH / name
                if src.exists() and src.is_dir():
                    exclude = opts.get("exclude", [])
                    for file_src, rel in collect_folder_files(src):
                        file_dst = dst / rel
                        # Only exclude if the file already exists in the destination
                        if file_dst.exists() and match_exclude_patterns(str(rel), exclude):
                            continue
                        if files_are_different(file_src, file_dst):
                            actions.append(
                                {
                                    "type": "file",
                                    "src": file_src,
                                    "dst": file_dst,
                                    "change_type": "new" if not file_dst.exists() else "updated",
                                }
                            )
        all_actions.append((target_dir, actions))
    return all_actions

def confirm_overwrite(summary: str) -> bool:
    print("The following files/folders will be overwritten/copied:\n")
    print(summary)
    resp = input("Proceed with these changes? [y/N]: ").strip().lower()
    return resp in ("y", "yes")

def perform_actions(actions: List[Tuple[Path, List[Dict[str, Any]]]], dry_run: bool = False) -> None:
    errors = []
    for target_dir, acts in actions:
        for act in acts:
            src, dst = act["src"], act["dst"]
            try:
                if dry_run:
                    continue
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
                print(f"Copied {src} -> {dst}")
            except Exception as e:
                print(f"[ERROR] {src} -> {dst}: {e}")
                errors.append((src, dst, str(e)))
    if errors:
        print("\nErrors encountered:")
        for src, dst, msg in errors:
            print(f"  {src} -> {dst}: {msg}")

def main():
    parser = argparse.ArgumentParser(description="Update project files/folders in all configured directories.")
    parser.add_argument("--yes", "--force", action="store_true", help="Skip confirmation prompt.")
    parser.add_argument("--dry-run", action="store_true", help="Preview actions without making changes.")
    parser.add_argument("--config", type=str, default=str(DEFAULT_CONFIG_PATH), help="Path to config_part_source.yaml.")
    args = parser.parse_args()

    config_path = Path(args.config)
    try:
        target_dirs = load_directories(config_path)
    except Exception as e:
        print(f"Failed to load directories from config: {e}")
        sys.exit(1)
    actions = build_copy_actions(target_dirs)
    total_changes = sum(len(acts) for _, acts in actions)
    if total_changes == 0:
        print("No changes to apply.")
        sys.exit(0)
    summary = summarize_actions(actions)
    if not args.yes and not args.dry_run:
        if not confirm_overwrite(summary):
            print("Aborted by user.")
            sys.exit(0)
    else:
        print(summary)
        if args.dry_run:
            print("(Dry run: no changes made)")
            sys.exit(0)
    perform_actions(actions, dry_run=args.dry_run)
    print("\nUpdate complete.")

if __name__ == "__main__":
    main()
