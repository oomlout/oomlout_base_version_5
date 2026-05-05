
# action_project_update_project.py — Detailed Implementation Plan

## 1. Load Target Directories
1.1. Open and read the YAML config file at `C:\od\OneDrive\docs\oomp_base\webserver\config_part_source.yaml`.
1.2. Parse the YAML and extract the list under the `directories` key.
1.3. For each directory:
  - If the path is relative, resolve it relative to the config file's parent directory.
  - Normalize all paths to absolute paths (as strings).
1.4. Store the list of target directories for later use.

## 2. Define Files/Folders to Copy
2.1. Create a Python dict named `PROJECT_UPDATE_ITEMS` (or similar) with the following structure:
  - Keys: names of files or folders to copy (e.g., 'working_oomp_populate.py', 'source_file', 'webserver')
  - Values: dicts with options, e.g.:
    - `type`: 'file' or 'folder'
    - `exclude`: list of glob patterns to exclude (for folders)
    - `always_include`: bool (if always included)
2.2. Set the source base directory to `C:\gh\project_base`.
2.3. Always include:
  - `working_oomp_populate.py` (file)
  - `source_file` (folder, no exclusions by default)
  - `webserver` (folder, with exclusions: `webserver/config_part_source.yaml`, `webserver/config_*.yaml`)
2.4. Allow easy manual editing of the dict to add/remove files/folders or exclusions.

## 3. Build and Summarize Copy Actions
3.1. For each target directory:
  - For each item in `PROJECT_UPDATE_ITEMS`:
    - Determine the source path (from project_base) and destination path (in target directory).
    - For folders, build a list of files/folders to copy, applying exclusions.
    - For files, check if the file exists in the source.
    - If the destination exists and will be overwritten, add to the overwrite list.
3.2. Collect all planned copy/overwrite actions for all target directories.
3.3. Before making any changes:
  - Print a summary:
    - Number of files/folders to be copied/overwritten per target directory.
    - Condensed lists (e.g., show up to 5 items, then '...and N more').
  - If not in --yes/--force mode, prompt the user ONCE for confirmation to proceed.
  - If --dry-run is specified, print the summary and exit without making changes.

## 4. Perform Copy Actions
4.1. For each planned action:
  - For files:
    - Copy the file from source to destination, overwriting if needed.
  - For folders:
    - Recursively copy the folder contents, skipping excluded files, overwriting existing files/folders.
  - If an error occurs (e.g., missing source, permission denied):
    - Print a warning message.
    - Continue with the next action.
4.2. After all actions, print a summary of what was copied, skipped, or failed.

## 5. Command-Line Options
5.1. Support the following command-line arguments:
  - `--yes` or `--force`: skip confirmation prompt and proceed with overwrites.
  - `--dry-run`: only print planned actions, do not copy or overwrite anything.
  - (Optional) `--config <path>`: override the default config YAML path.

## 6. Error Handling
6.1. For any error (missing source, permission issues, etc.):
  - Print a clear warning with the file/folder and error message.
  - Continue processing remaining actions.
6.2. At the end, print a summary of all errors encountered.

---

This detailed plan will be followed for the implementation of action_project_update_project.py. Progress markers will be updated as development proceeds.