@echo off
setlocal EnableExtensions
set "ROOT_DIR=%~dp0"
set "LOG_FILE=%~dp0action_oomp_run_all_errors.log"
if exist "%LOG_FILE%" del "%LOG_FILE%"
echo Running action_make_action_only.py for configured part sources.
echo Logging errors to %LOG_FILE%.
echo.

call :run_repo "C:\od\OneDrive\docs\oomp_base\parts"

call :run_repo "C:\od\OneDrive\docs\household_document_base"

call :run_repo "C:\od\OneDrive\docs\oomp_furniture"

call :run_repo "C:\od\OneDrive\docs\oomp_tool"

call :run_repo "C:\od\OneDrive\docs\oomp_paper"

call :run_repo "C:\od\OneDrive\docs\warehouse_storage_tote"

call :run_repo "C:\gh\oomp_paper_sheet"

call :run_repo "C:\gh\oomp_hardware_screw_version_5"

call :run_repo "C:\gh\oomp_electrical_extension_lead_uk_socket_6_outlet_pro_elec_2068_version_5"

echo.
echo Finished processing all configured part sources.
exit /b 0

:run_repo
set "TARGET_DIR=%~1"
echo ========================================
echo Processing %TARGET_DIR%
if not exist "%TARGET_DIR%" (
    echo [missing_dir] %TARGET_DIR%>>"%LOG_FILE%"
    echo Missing directory, skipping.
    exit /b 0
)
if not exist "%TARGET_DIR%\action_make_action_only.py" (
    echo [missing_script] %TARGET_DIR%\action_make_action_only.py>>"%LOG_FILE%"
    echo action_make_action_only.py not found, skipping.
    exit /b 0
)
pushd "%TARGET_DIR%" >nul
"C:\Users\aaron\AppData\Local\Programs\Python\Python312\python.exe" action_make_action_only.py
set "RUN_ERROR=%ERRORLEVEL%"
popd >nul
if not "%RUN_ERROR%"=="0" (
    echo [error %RUN_ERROR%] %TARGET_DIR%>>"%LOG_FILE%"
    echo action_make_action_only.py failed with exit code %RUN_ERROR%.
    exit /b 0
)
echo Completed successfully.
exit /b 0
