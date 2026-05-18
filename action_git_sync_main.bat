@echo off
setlocal EnableExtensions
echo Pulling configured repositories.
echo.

echo [parts]
if not exist "C:\od\OneDrive\docs\parts" (
    echo   skipped: folder does not exist at C:\od\OneDrive\docs\parts
) else if not exist "C:\od\OneDrive\docs\parts\.git" (
    echo   skipped: not a git repository at C:\od\OneDrive\docs\parts
) else (
    git -C "C:\od\OneDrive\docs\parts" pull
)
echo.

echo [computer_base]
if not exist "C:\od\OneDrive\docs\computer_base" (
    echo   skipped: folder does not exist at C:\od\OneDrive\docs\computer_base
) else if not exist "C:\od\OneDrive\docs\computer_base\.git" (
    echo   skipped: not a git repository at C:\od\OneDrive\docs\computer_base
) else (
    git -C "C:\od\OneDrive\docs\computer_base" pull
)
echo.

echo [oomp_furniture]
if not exist "C:\od\OneDrive\docs\oomp_furniture" (
    echo   skipped: folder does not exist at C:\od\OneDrive\docs\oomp_furniture
) else if not exist "C:\od\OneDrive\docs\oomp_furniture\.git" (
    echo   skipped: not a git repository at C:\od\OneDrive\docs\oomp_furniture
) else (
    git -C "C:\od\OneDrive\docs\oomp_furniture" pull
)
echo.

echo [oomp_tool]
if not exist "C:\od\OneDrive\docs\oomp_tool" (
    echo   skipped: folder does not exist at C:\od\OneDrive\docs\oomp_tool
) else if not exist "C:\od\OneDrive\docs\oomp_tool\.git" (
    echo   skipped: not a git repository at C:\od\OneDrive\docs\oomp_tool
) else (
    git -C "C:\od\OneDrive\docs\oomp_tool" pull
)
echo.

echo [project_bolt_packaging]
if not exist "C:\od\OneDrive\docs\project_bolt_packaging" (
    echo   skipped: folder does not exist at C:\od\OneDrive\docs\project_bolt_packaging
) else if not exist "C:\od\OneDrive\docs\project_bolt_packaging\.git" (
    echo   skipped: not a git repository at C:\od\OneDrive\docs\project_bolt_packaging
) else (
    git -C "C:\od\OneDrive\docs\project_bolt_packaging" pull
)
echo.

echo [project_bolt_base]
if not exist "C:\od\OneDrive\docs\project_bolt_base" (
    echo   skipped: folder does not exist at C:\od\OneDrive\docs\project_bolt_base
) else if not exist "C:\od\OneDrive\docs\project_bolt_base\.git" (
    echo   skipped: not a git repository at C:\od\OneDrive\docs\project_bolt_base
) else (
    git -C "C:\od\OneDrive\docs\project_bolt_base" pull
)
echo.

echo [oomp_packaging]
if not exist "C:\od\OneDrive\docs\oomp_packaging" (
    echo   skipped: folder does not exist at C:\od\OneDrive\docs\oomp_packaging
) else if not exist "C:\od\OneDrive\docs\oomp_packaging\.git" (
    echo   skipped: not a git repository at C:\od\OneDrive\docs\oomp_packaging
) else (
    git -C "C:\od\OneDrive\docs\oomp_packaging" pull
)
echo.

echo [phone_base]
if not exist "C:\od\OneDrive\docs\phone_base" (
    echo   skipped: folder does not exist at C:\od\OneDrive\docs\phone_base
) else if not exist "C:\od\OneDrive\docs\phone_base\.git" (
    echo   skipped: not a git repository at C:\od\OneDrive\docs\phone_base
) else (
    git -C "C:\od\OneDrive\docs\phone_base" pull
)
echo.

echo [warehouse_storage_tote]
if not exist "C:\od\OneDrive\docs\warehouse_storage_tote" (
    echo   skipped: folder does not exist at C:\od\OneDrive\docs\warehouse_storage_tote
) else if not exist "C:\od\OneDrive\docs\warehouse_storage_tote\.git" (
    echo   skipped: not a git repository at C:\od\OneDrive\docs\warehouse_storage_tote
) else (
    git -C "C:\od\OneDrive\docs\warehouse_storage_tote" pull
)
echo.

echo [household_document_base]
if not exist "C:\od\OneDrive\docs\household_document_base" (
    echo   skipped: folder does not exist at C:\od\OneDrive\docs\household_document_base
) else if not exist "C:\od\OneDrive\docs\household_document_base\.git" (
    echo   skipped: not a git repository at C:\od\OneDrive\docs\household_document_base
) else (
    git -C "C:\od\OneDrive\docs\household_document_base" pull
)
echo.

echo [project_base]
if not exist "C:\gh\project_base" (
    echo   skipped: folder does not exist at C:\gh\project_base
) else if not exist "C:\gh\project_base\.git" (
    echo   skipped: not a git repository at C:\gh\project_base
) else (
    git -C "C:\gh\project_base" pull
)
echo.

echo [oomp_paper_sheet]
if not exist "C:\gh\oomp_paper_sheet" (
    echo   skipped: folder does not exist at C:\gh\oomp_paper_sheet
) else if not exist "C:\gh\oomp_paper_sheet\.git" (
    echo   skipped: not a git repository at C:\gh\oomp_paper_sheet
) else (
    git -C "C:\gh\oomp_paper_sheet" pull
)
echo.

echo [oomp_hardware_screw_version_5]
if not exist "C:\gh\oomp_hardware_screw_version_5" (
    echo   skipped: folder does not exist at C:\gh\oomp_hardware_screw_version_5
) else if not exist "C:\gh\oomp_hardware_screw_version_5\.git" (
    echo   skipped: not a git repository at C:\gh\oomp_hardware_screw_version_5
) else (
    git -C "C:\gh\oomp_hardware_screw_version_5" pull
)
echo.

echo [oomp_hardware_bolt_version_5]
if not exist "C:\gh\oomp_hardware_bolt_version_5" (
    echo   skipped: folder does not exist at C:\gh\oomp_hardware_bolt_version_5
) else if not exist "C:\gh\oomp_hardware_bolt_version_5\.git" (
    echo   skipped: not a git repository at C:\gh\oomp_hardware_bolt_version_5
) else (
    git -C "C:\gh\oomp_hardware_bolt_version_5" pull
)
echo.

echo [oomp_electrical_extension_lead_uk_socket_6_outlet_pro_elec_2068_version_5]
if not exist "C:\gh\oomp_electrical_extension_lead_uk_socket_6_outlet_pro_elec_2068_version_5" (
    echo   skipped: folder does not exist at C:\gh\oomp_electrical_extension_lead_uk_socket_6_outlet_pro_elec_2068_version_5
) else if not exist "C:\gh\oomp_electrical_extension_lead_uk_socket_6_outlet_pro_elec_2068_version_5\.git" (
    echo   skipped: not a git repository at C:\gh\oomp_electrical_extension_lead_uk_socket_6_outlet_pro_elec_2068_version_5
) else (
    git -C "C:\gh\oomp_electrical_extension_lead_uk_socket_6_outlet_pro_elec_2068_version_5" pull
)
echo.

echo [oomlout_base_version_5]
if not exist "C:\gh\oomlout_base_version_5" (
    echo   skipped: folder does not exist at C:\gh\oomlout_base_version_5
) else if not exist "C:\gh\oomlout_base_version_5\.git" (
    echo   skipped: not a git repository at C:\gh\oomlout_base_version_5
) else (
    git -C "C:\gh\oomlout_base_version_5" pull
)
echo.

echo [oomlout_oobb_version_5]
if not exist "C:\gh\oomlout_oobb_version_5" (
    echo   skipped: folder does not exist at C:\gh\oomlout_oobb_version_5
) else if not exist "C:\gh\oomlout_oobb_version_5\.git" (
    echo   skipped: not a git repository at C:\gh\oomlout_oobb_version_5
) else (
    git -C "C:\gh\oomlout_oobb_version_5" pull
)
echo.

exit /b 0
