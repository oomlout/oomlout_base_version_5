@echo off
setlocal

set "github_desktop_dir=%LOCALAPPDATA%\GitHubDesktop"
set "github_desktop_app_dir="

for /f "usebackq delims=" %%I in (`powershell -NoProfile -Command "$base = Join-Path $env:LOCALAPPDATA 'GitHubDesktop'; Get-ChildItem -Path $base -Directory -Filter 'app-*' | Sort-Object { [version]($_.Name -replace '^app-','') } -Descending | Select-Object -First 1 -ExpandProperty FullName"`) do set "github_desktop_app_dir=%%I"

if not defined github_desktop_app_dir (
	echo Could not find a GitHub Desktop app-* directory in "%github_desktop_dir%".
	exit /b 1
)

cd /d "%github_desktop_app_dir%\resources\app\git\cmd"
git config --system core.longpaths true

echo Successfully set core.longpaths to true. on %date% at %time% in %github_desktop_app_dir%