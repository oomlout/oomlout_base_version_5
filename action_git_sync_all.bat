@echo off
setlocal enabledelayedexpansion

set BASE_DIR=c:\gh
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

set FAILED_FOLDERS=
set SUCCESS_COUNT=0
set FAIL_COUNT=0

echo ============================================================
echo  Git Pull All Repos in %BASE_DIR%
echo ============================================================
echo.

for /d %%F in ("%BASE_DIR%\*") do (
    if exist "%%F\.git" (
        echo Pulling: %%~nxF
        pushd "%%F"
        git pull --ff-only 2>&1
        if !errorlevel! neq 0 (
            set /a FAIL_COUNT+=1
            set FAILED_FOLDERS=!FAILED_FOLDERS! "%%~nxF"
        ) else (
            set /a SUCCESS_COUNT+=1
        )
        popd
        echo.
    )
)

echo ============================================================
echo  REPORT
echo ============================================================
echo  Successful pulls : %SUCCESS_COUNT%
echo  Failed pulls     : %FAIL_COUNT%
echo.
set EXIT_CODE=0
if "%FAIL_COUNT%"=="0" (
    echo  All repositories pulled successfully.
) else (
    set EXIT_CODE=1
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
