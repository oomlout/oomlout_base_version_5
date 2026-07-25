@echo off
setlocal enabledelayedexpansion

set "BASE_DIR=c:\gh"
set "SCRIPT_DIR=%~dp0"
set "COMMIT_MESSAGE=auto-cvomitt"
set "END_TIMEOUT_SECONDS=%~1"
set "INVALID_TIMEOUT="

if not "%END_TIMEOUT_SECONDS%"=="" (
    for /f "delims=0123456789" %%A in ("%END_TIMEOUT_SECONDS%") do set "INVALID_TIMEOUT=1"
    if defined INVALID_TIMEOUT (
        echo Invalid timeout value: %END_TIMEOUT_SECONDS%
        echo Use a non-negative integer number of seconds.
        endlocal
        exit /b 2
    )
)

echo ============================================================
echo  Sync Before Push
echo ============================================================
echo.
call "%SCRIPT_DIR%action_git_sync_all.bat" 0
if errorlevel 1 (
    echo Sync step failed. Aborting commit and push.
    if "%END_TIMEOUT_SECONDS%"=="" (
        pause
    ) else if not "%END_TIMEOUT_SECONDS%"=="0" (
        timeout /t %END_TIMEOUT_SECONDS% /nobreak >nul
    )
    endlocal
    exit /b 1
)

set "FAILED_FOLDERS="
set /a SUCCESS_COUNT=0
set /a FAIL_COUNT=0

echo.
echo ============================================================
echo  Commit And Push All Repos In %BASE_DIR%
echo ============================================================
echo.

for /d %%F in ("%BASE_DIR%\*") do (
    if exist "%%F\.git" (
        echo Processing: %%~nxF
        pushd "%%F"
        set "REPO_FAILED=0"

        git add -A
        if !errorlevel! neq 0 (
            echo   failed: git add
            set /a FAIL_COUNT+=1
            set FAILED_FOLDERS=!FAILED_FOLDERS! "%%~nxF"
            set "REPO_FAILED=1"
        )

        if "!REPO_FAILED!"=="0" (
            git diff --cached --quiet
            if !errorlevel! neq 0 (
                git commit -m "%COMMIT_MESSAGE%"
                if !errorlevel! neq 0 (
                    echo   failed: git commit
                    set /a FAIL_COUNT+=1
                    set FAILED_FOLDERS=!FAILED_FOLDERS! "%%~nxF"
                    set "REPO_FAILED=1"
                )
            ) else (
                echo   no local changes to commit
            )
        )

        if "!REPO_FAILED!"=="0" (
            git push
            if !errorlevel! neq 0 (
                echo   failed: git push
                set /a FAIL_COUNT+=1
                set FAILED_FOLDERS=!FAILED_FOLDERS! "%%~nxF"
            ) else (
                set /a SUCCESS_COUNT+=1
            )
        )

        popd
        echo.
    )
)

echo ============================================================
echo  REPORT
echo ============================================================
echo  Successful pushes : %SUCCESS_COUNT%
echo  Failed pushes     : %FAIL_COUNT%
echo.
set "EXIT_CODE=0"
if "%FAIL_COUNT%"=="0" (
    echo  All repositories pushed successfully.
) else (
    set "EXIT_CODE=1"
    echo  The following folders failed:
    for %%F in (%FAILED_FOLDERS%) do (
        echo    - %%~F
    )
)
echo ============================================================
echo.

if "%END_TIMEOUT_SECONDS%"=="" (
    pause
) else (
    if "%END_TIMEOUT_SECONDS%"=="0" (
        echo Continuing immediately.
    ) else (
        echo Continuing in %END_TIMEOUT_SECONDS% seconds...
        timeout /t %END_TIMEOUT_SECONDS% /nobreak >nul
    )
)

endlocal & exit /b %EXIT_CODE%
