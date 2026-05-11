import argparse
import subprocess
from pathlib import Path


BASE_DIRECTORY = Path("c:/gh")
REPOSITORIES = [
    "oomlout_base_version_5",
    "oomlout_media",
    "oomlout_oobb_version_5",
    "oomlout_oomp_version_5",
    "oomlout_roboclick",
    "oomp_paper_sheet",    
    "oomp_hardware_screw_version_5",    
    "oomp_hardware_bolt_version_5",    
]


def sync_repository(repo_name: str, base_directory: Path, dry_run: bool) -> bool:
    repo_path = base_directory / repo_name
    print(f"\n[{repo_name}] {repo_path}")

    if not repo_path.exists():
        print("  skipped: folder does not exist")
        return False

    if not (repo_path / ".git").exists():
        print("  skipped: not a git repository")
        return False

    command = ["git", "-C", str(repo_path), "pull"]
    if dry_run:
        print(f"  dry run: {' '.join(command)}")
        return True

    result = subprocess.run(command, check=False)
    if result.returncode != 0:
        print(f"  failed with exit code {result.returncode}")
        return False

    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Pull the main oomlout repositories.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the git commands without running them.",
    )
    args = parser.parse_args()

    success_count = 0
    for repo_name in REPOSITORIES:
        if sync_repository(repo_name, BASE_DIRECTORY, args.dry_run):
            success_count += 1

    print(f"\nProcessed {len(REPOSITORIES)} repositories, successful actions: {success_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())