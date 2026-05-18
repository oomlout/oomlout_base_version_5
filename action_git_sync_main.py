from __future__ import annotations

import argparse
import subprocess
from pathlib import Path
from typing import Any

import yaml


DEFAULT_CONFIG_PATH = Path(r"C:\od\OneDrive\docs\oomp_base\config_part_source.yaml")
DEFAULT_GITHUB_REPOS_PATH = Path(__file__).with_name("github_repos.yaml")
DEFAULT_SETUP_BATCH_PATH = Path(__file__).with_name("action_git_clone_setup.bat")
DEFAULT_SYNC_BATCH_PATH = Path(__file__).with_name("action_git_sync_main.bat")
ADDITIONAL_REPOSITORY_DIRECTORIES = [
    Path(r"C:\gh\oomlout_base_version_5"),
    Path(r"C:\gh\oomlout_oobb_version_5"),
]


def normalize_repository_path(directory: str, config_base_directory: Path) -> Path:
    repo_path = Path(directory.strip())
    if not repo_path.is_absolute():
        repo_path = (config_base_directory / repo_path).resolve()
    return repo_path


def append_unique_path(repository_paths: list[Path], seen_paths: set[Path], repo_path: Path) -> None:
    if repo_path in seen_paths:
        return

    seen_paths.add(repo_path)
    repository_paths.append(repo_path)


def load_repository_paths(config_path: Path, additional_directories: list[Path] | None = None) -> list[Path]:
    with config_path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle) or {}

    directories = config.get("directories", [])
    if not isinstance(directories, list):
        raise ValueError("Expected 'directories' to be a list in config_part_source.yaml")

    config_base_directory = config_path.parent.parent
    repository_paths: list[Path] = []
    seen_paths: set[Path] = set()
    for directory in directories:
        if not isinstance(directory, str):
            raise ValueError(f"Directory entries must be strings, got: {directory!r}")

        cleaned_directory = directory.strip()
        if not cleaned_directory:
            continue

        repo_path = normalize_repository_path(cleaned_directory, config_base_directory)
        append_unique_path(repository_paths, seen_paths, repo_path)

    for repo_path in additional_directories or []:
        append_unique_path(repository_paths, seen_paths, repo_path)

    return repository_paths


def load_github_repositories(github_repos_path: Path) -> dict[str, dict[str, Any]]:
    if not github_repos_path.exists():
        return {}

    with github_repos_path.open("r", encoding="utf-8") as handle:
        github_repositories = yaml.safe_load(handle) or {}

    if not isinstance(github_repositories, dict):
        raise ValueError("Expected github_repos.yaml to contain a mapping of repositories")

    normalized_repositories: dict[str, dict[str, Any]] = {}
    for repo_id, repo_data in github_repositories.items():
        if not isinstance(repo_data, dict):
            continue

        name = repo_data.get("name", repo_id)
        if isinstance(name, str) and name.strip():
            normalized_repositories[name.strip()] = repo_data

    return normalized_repositories


def get_clone_url(repo_name: str, github_repositories: dict[str, dict[str, Any]]) -> str:
    repo_data = github_repositories.get(repo_name, {})
    url = repo_data.get("url")
    if isinstance(url, str) and url.strip():
        return url.strip()

    return f"https://github.com/oomlout/{repo_name}.git"


def build_setup_batch(repository_paths: list[Path], github_repositories: dict[str, dict[str, Any]]) -> str:
    lines = [
        "@echo off",
        "setlocal EnableExtensions",
        "echo Cloning configured repositories.",
        "echo.",
        "",
    ]

    for repo_path in repository_paths:
        repo_name = repo_path.name
        parent_directory = str(repo_path.parent).replace('"', '""')
        target_directory = str(repo_path).replace('"', '""')
        clone_url = get_clone_url(repo_name, github_repositories).replace('"', '""')
        lines.extend(
            [
                f"echo [{repo_name}]",
                f"if exist \"{target_directory}\\.git\" (",
                f"    echo   skipping: already cloned at {target_directory}",
                f") else if exist \"{target_directory}\" (",
                f"    echo   skipping: target folder already exists at {target_directory}",
                ") else (",
                f"    if not exist \"{parent_directory}\" mkdir \"{parent_directory}\"",
                f"    git clone \"{clone_url}\" \"{target_directory}\"",
                ")",
                "echo.",
                "",
            ]
        )

    lines.append("exit /b 0")
    return "\r\n".join(lines) + "\r\n"


def write_setup_batch(
    repository_paths: list[Path],
    github_repositories: dict[str, dict[str, Any]],
    output_path: Path,
) -> None:
    batch_contents = build_setup_batch(repository_paths, github_repositories)
    output_path.write_text(batch_contents, encoding="utf-8", newline="")


def build_sync_batch(repository_paths: list[Path]) -> str:
    lines = [
        "@echo off",
        "setlocal EnableExtensions",
        "echo Pulling configured repositories.",
        "echo.",
        "",
    ]

    for repo_path in repository_paths:
        escaped_repo_path = str(repo_path).replace('"', '""')
        repo_name = repo_path.name
        lines.extend(
            [
                f"echo [{repo_name}]",
                f"if not exist \"{escaped_repo_path}\" (",
                f"    echo   skipped: folder does not exist at {escaped_repo_path}",
                f") else if not exist \"{escaped_repo_path}\\.git\" (",
                f"    echo   skipped: not a git repository at {escaped_repo_path}",
                ") else (",
                f"    git -C \"{escaped_repo_path}\" pull",
                ")",
                "echo.",
                "",
            ]
        )

    lines.append("exit /b 0")
    return "\r\n".join(lines) + "\r\n"


def write_sync_batch(repository_paths: list[Path], output_path: Path) -> None:
    batch_contents = build_sync_batch(repository_paths)
    output_path.write_text(batch_contents, encoding="utf-8", newline="")


def sync_repository(repo_path: Path, dry_run: bool) -> bool:
    repo_name = repo_path.name
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
    parser = argparse.ArgumentParser(description="Pull repositories listed in config_part_source.yaml.")
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Path to config_part_source.yaml.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the git commands without running them.",
    )
    parser.add_argument(
        "--write-setup-bat",
        action="store_true",
        help="Write a batch file that clones the configured repositories.",
    )
    parser.add_argument(
        "--write-sync-bat",
        action="store_true",
        help="Write a batch file that pulls the configured repositories.",
    )
    parser.add_argument(
        "--setup-bat-path",
        type=Path,
        default=DEFAULT_SETUP_BATCH_PATH,
        help="Path for the generated clone setup batch file.",
    )
    parser.add_argument(
        "--sync-bat-path",
        type=Path,
        default=DEFAULT_SYNC_BATCH_PATH,
        help="Path for the generated sync batch file.",
    )
    parser.add_argument(
        "--github-repos",
        type=Path,
        default=DEFAULT_GITHUB_REPOS_PATH,
        help="Path to github_repos.yaml used for clone URL overrides.",
    )
    args = parser.parse_args()

    repository_paths = load_repository_paths(args.config, ADDITIONAL_REPOSITORY_DIRECTORIES)

    if args.write_setup_bat:
        github_repositories = load_github_repositories(args.github_repos)
        write_setup_batch(repository_paths, github_repositories, args.setup_bat_path)
        print(f"Wrote setup batch: {args.setup_bat_path}")

    if args.write_sync_bat:
        write_sync_batch(repository_paths, args.sync_bat_path)
        print(f"Wrote sync batch: {args.sync_bat_path}")

    success_count = 0
    for repo_path in repository_paths:
        if sync_repository(repo_path, args.dry_run):
            success_count += 1

    print(f"\nProcessed {len(repository_paths)} repositories, successful actions: {success_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())