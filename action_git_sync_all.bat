@echo off
setlocal enabledelayedexpansion

set BASE_DIR=c:\gh

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
        git pull 2>&1
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
if "%FAIL_COUNT%"=="0" (
    echo  All repositories pulled successfully.
) else (
    echo  The following folders failed:
    for %%F in (%FAILED_FOLDERS%) do (
        echo    - %%~F
    )
)
echo ============================================================
echo.
pause
endlocal
