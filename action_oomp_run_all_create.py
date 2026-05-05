from __future__ import annotations

from pathlib import Path
import sys

import yaml


CONFIG_PATH = Path(r"C:\od\OneDrive\docs\oomp_base\webserver\config_part_source.yaml")
CONFIG_BASE_DIRECTORY = CONFIG_PATH.parent.parent
OUTPUT_PATH = Path(__file__).with_name("action_oomp_run_all.bat")
LOG_FILE_NAME = "action_oomp_run_all_errors.log"
PYTHON_EXECUTABLE = str(Path(sys.executable))


def load_directories(config_path: Path) -> list[str]:
    with config_path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle) or {}

    directories = config.get("directories", [])
    if not isinstance(directories, list):
        raise ValueError("Expected 'directories' to be a list in config_part_source.yaml")

    normalized_directories: list[str] = []
    for directory in directories:
        if not isinstance(directory, str):
            raise ValueError(f"Directory entries must be strings, got: {directory!r}")
        cleaned_directory = directory.strip()
        if cleaned_directory:
            resolved_directory = Path(cleaned_directory)
            if not resolved_directory.is_absolute():
                resolved_directory = (CONFIG_BASE_DIRECTORY / resolved_directory).resolve()
            normalized_directories.append(str(resolved_directory))

    return normalized_directories


def build_batch_contents(directories: list[str]) -> str:
    lines = [
        "@echo off",
        "setlocal EnableExtensions",
        "set \"ROOT_DIR=%~dp0\"",
        f"set \"LOG_FILE=%~dp0{LOG_FILE_NAME}\"",
        "if exist \"%LOG_FILE%\" del \"%LOG_FILE%\"",
        "echo Running action_make_all.py for configured part sources.",
        "echo Logging errors to %LOG_FILE%.",
        "echo.",
        "",
    ]

    for directory in directories:
        escaped_directory = directory.replace('"', '""')
        lines.extend(
            [
                f"call :run_repo \"{escaped_directory}\"",
                "",
            ]
        )

    lines.extend(
        [
            "echo.",
            "echo Finished processing all configured part sources.",
            "exit /b 0",
            "",
            ":run_repo",
            "set \"TARGET_DIR=%~1\"",
            "echo ========================================",
            "echo Processing %TARGET_DIR%",
            "if not exist \"%TARGET_DIR%\" (",
            "    echo [missing_dir] %TARGET_DIR%>>\"%LOG_FILE%\"",
            "    echo Missing directory, skipping.",
            "    exit /b 0",
            ")",
            "if not exist \"%TARGET_DIR%\\action_make_all.py\" (",
            "    echo [missing_script] %TARGET_DIR%\\action_make_all.py>>\"%LOG_FILE%\"",
            "    echo action_make_all.py not found, skipping.",
            "    exit /b 0",
            ")",
            "pushd \"%TARGET_DIR%\" >nul",
            f'"{PYTHON_EXECUTABLE}" action_make_all.py',
            "set \"RUN_ERROR=%ERRORLEVEL%\"",
            "popd >nul",
            "if not \"%RUN_ERROR%\"==\"0\" (",
            "    echo [error %RUN_ERROR%] %TARGET_DIR%>>\"%LOG_FILE%\"",
            "    echo action_make_all.py failed with exit code %RUN_ERROR%.",
            "    exit /b 0",
            ")",
            "echo Completed successfully.",
            "exit /b 0",
        ]
    )

    return "\r\n".join(lines) + "\r\n"


def main() -> int:
    directories = load_directories(CONFIG_PATH)
    batch_contents = build_batch_contents(directories)
    OUTPUT_PATH.write_text(batch_contents, encoding="utf-8", newline="")
    print(f"Wrote {OUTPUT_PATH} for {len(directories)} directories.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())