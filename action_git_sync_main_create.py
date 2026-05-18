from __future__ import annotations

from action_git_sync_main import (
    ADDITIONAL_REPOSITORY_DIRECTORIES,
    DEFAULT_CONFIG_PATH,
    DEFAULT_GITHUB_REPOS_PATH,
    DEFAULT_SETUP_BATCH_PATH,
    DEFAULT_SYNC_BATCH_PATH,
    load_github_repositories,
    load_repository_paths,
    write_setup_batch,
    write_sync_batch,
)


def main() -> int:
    repository_paths = load_repository_paths(DEFAULT_CONFIG_PATH, ADDITIONAL_REPOSITORY_DIRECTORIES)
    github_repositories = load_github_repositories(DEFAULT_GITHUB_REPOS_PATH)

    write_setup_batch(repository_paths, github_repositories, DEFAULT_SETUP_BATCH_PATH)
    write_sync_batch(repository_paths, DEFAULT_SYNC_BATCH_PATH)

    print(f"Wrote {DEFAULT_SETUP_BATCH_PATH} for {len(repository_paths)} repositories.")
    print(f"Wrote {DEFAULT_SYNC_BATCH_PATH} for {len(repository_paths)} repositories.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())