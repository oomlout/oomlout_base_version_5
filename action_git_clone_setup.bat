@echo off
setlocal EnableExtensions
echo Cloning configured repositories.
echo.

echo [parts]
if exist "C:\od\OneDrive\docs\parts\.git" (
    echo   skipping: already cloned at C:\od\OneDrive\docs\parts
) else if exist "C:\od\OneDrive\docs\parts" (
    echo   skipping: target folder already exists at C:\od\OneDrive\docs\parts
) else (
    if not exist "C:\od\OneDrive\docs" mkdir "C:\od\OneDrive\docs"
    git clone "https://github.com/oomlout/parts.git" "C:\od\OneDrive\docs\parts"
)
echo.

echo [computer_base]
if exist "C:\od\OneDrive\docs\computer_base\.git" (
    echo   skipping: already cloned at C:\od\OneDrive\docs\computer_base
) else if exist "C:\od\OneDrive\docs\computer_base" (
    echo   skipping: target folder already exists at C:\od\OneDrive\docs\computer_base
) else (
    if not exist "C:\od\OneDrive\docs" mkdir "C:\od\OneDrive\docs"
    git clone "https://github.com/oomlout/computer_base.git" "C:\od\OneDrive\docs\computer_base"
)
echo.

echo [oomp_furniture]
if exist "C:\od\OneDrive\docs\oomp_furniture\.git" (
    echo   skipping: already cloned at C:\od\OneDrive\docs\oomp_furniture
) else if exist "C:\od\OneDrive\docs\oomp_furniture" (
    echo   skipping: target folder already exists at C:\od\OneDrive\docs\oomp_furniture
) else (
    if not exist "C:\od\OneDrive\docs" mkdir "C:\od\OneDrive\docs"
    git clone "https://github.com/oomlout/oomp_furniture.git" "C:\od\OneDrive\docs\oomp_furniture"
)
echo.

echo [oomp_tool]
if exist "C:\od\OneDrive\docs\oomp_tool\.git" (
    echo   skipping: already cloned at C:\od\OneDrive\docs\oomp_tool
) else if exist "C:\od\OneDrive\docs\oomp_tool" (
    echo   skipping: target folder already exists at C:\od\OneDrive\docs\oomp_tool
) else (
    if not exist "C:\od\OneDrive\docs" mkdir "C:\od\OneDrive\docs"
    git clone "https://github.com/oomlout/oomp_tool.git" "C:\od\OneDrive\docs\oomp_tool"
)
echo.

echo [project_bolt_packaging]
if exist "C:\od\OneDrive\docs\project_bolt_packaging\.git" (
    echo   skipping: already cloned at C:\od\OneDrive\docs\project_bolt_packaging
) else if exist "C:\od\OneDrive\docs\project_bolt_packaging" (
    echo   skipping: target folder already exists at C:\od\OneDrive\docs\project_bolt_packaging
) else (
    if not exist "C:\od\OneDrive\docs" mkdir "C:\od\OneDrive\docs"
    git clone "https://github.com/oomlout/project_bolt_packaging.git" "C:\od\OneDrive\docs\project_bolt_packaging"
)
echo.

echo [project_bolt_base]
if exist "C:\od\OneDrive\docs\project_bolt_base\.git" (
    echo   skipping: already cloned at C:\od\OneDrive\docs\project_bolt_base
) else if exist "C:\od\OneDrive\docs\project_bolt_base" (
    echo   skipping: target folder already exists at C:\od\OneDrive\docs\project_bolt_base
) else (
    if not exist "C:\od\OneDrive\docs" mkdir "C:\od\OneDrive\docs"
    git clone "https://github.com/oomlout/project_bolt_base.git" "C:\od\OneDrive\docs\project_bolt_base"
)
echo.

echo [oomp_packaging]
if exist "C:\od\OneDrive\docs\oomp_packaging\.git" (
    echo   skipping: already cloned at C:\od\OneDrive\docs\oomp_packaging
) else if exist "C:\od\OneDrive\docs\oomp_packaging" (
    echo   skipping: target folder already exists at C:\od\OneDrive\docs\oomp_packaging
) else (
    if not exist "C:\od\OneDrive\docs" mkdir "C:\od\OneDrive\docs"
    git clone "https://github.com/oomlout/oomp_packaging.git" "C:\od\OneDrive\docs\oomp_packaging"
)
echo.

echo [phone_base]
if exist "C:\od\OneDrive\docs\phone_base\.git" (
    echo   skipping: already cloned at C:\od\OneDrive\docs\phone_base
) else if exist "C:\od\OneDrive\docs\phone_base" (
    echo   skipping: target folder already exists at C:\od\OneDrive\docs\phone_base
) else (
    if not exist "C:\od\OneDrive\docs" mkdir "C:\od\OneDrive\docs"
    git clone "https://github.com/oomlout/phone_base.git" "C:\od\OneDrive\docs\phone_base"
)
echo.

echo [warehouse_storage_tote]
if exist "C:\od\OneDrive\docs\warehouse_storage_tote\.git" (
    echo   skipping: already cloned at C:\od\OneDrive\docs\warehouse_storage_tote
) else if exist "C:\od\OneDrive\docs\warehouse_storage_tote" (
    echo   skipping: target folder already exists at C:\od\OneDrive\docs\warehouse_storage_tote
) else (
    if not exist "C:\od\OneDrive\docs" mkdir "C:\od\OneDrive\docs"
    git clone "https://github.com/oomlout/warehouse_storage_tote.git" "C:\od\OneDrive\docs\warehouse_storage_tote"
)
echo.

echo [household_document_base]
if exist "C:\od\OneDrive\docs\household_document_base\.git" (
    echo   skipping: already cloned at C:\od\OneDrive\docs\household_document_base
) else if exist "C:\od\OneDrive\docs\household_document_base" (
    echo   skipping: target folder already exists at C:\od\OneDrive\docs\household_document_base
) else (
    if not exist "C:\od\OneDrive\docs" mkdir "C:\od\OneDrive\docs"
    git clone "https://github.com/oomlout/household_document_base.git" "C:\od\OneDrive\docs\household_document_base"
)
echo.

echo [project_base]
if exist "C:\gh\project_base\.git" (
    echo   skipping: already cloned at C:\gh\project_base
) else if exist "C:\gh\project_base" (
    echo   skipping: target folder already exists at C:\gh\project_base
) else (
    if not exist "C:\gh" mkdir "C:\gh"
    git clone "https://github.com/oomlout/project_base.git" "C:\gh\project_base"
)
echo.

echo [oomp_paper_sheet]
if exist "C:\gh\oomp_paper_sheet\.git" (
    echo   skipping: already cloned at C:\gh\oomp_paper_sheet
) else if exist "C:\gh\oomp_paper_sheet" (
    echo   skipping: target folder already exists at C:\gh\oomp_paper_sheet
) else (
    if not exist "C:\gh" mkdir "C:\gh"
    git clone "https://github.com/oomlout/oomp_paper_sheet.git" "C:\gh\oomp_paper_sheet"
)
echo.

echo [oomp_hardware_screw_version_5]
if exist "C:\gh\oomp_hardware_screw_version_5\.git" (
    echo   skipping: already cloned at C:\gh\oomp_hardware_screw_version_5
) else if exist "C:\gh\oomp_hardware_screw_version_5" (
    echo   skipping: target folder already exists at C:\gh\oomp_hardware_screw_version_5
) else (
    if not exist "C:\gh" mkdir "C:\gh"
    git clone "https://github.com/oomlout/oomp_hardware_screw_version_5.git" "C:\gh\oomp_hardware_screw_version_5"
)
echo.

echo [oomp_hardware_bolt_version_5]
if exist "C:\gh\oomp_hardware_bolt_version_5\.git" (
    echo   skipping: already cloned at C:\gh\oomp_hardware_bolt_version_5
) else if exist "C:\gh\oomp_hardware_bolt_version_5" (
    echo   skipping: target folder already exists at C:\gh\oomp_hardware_bolt_version_5
) else (
    if not exist "C:\gh" mkdir "C:\gh"
    git clone "https://github.com/oomlout/oomp_hardware_bolt_version_5.git" "C:\gh\oomp_hardware_bolt_version_5"
)
echo.

echo [oomp_electrical_extension_lead_uk_socket_6_outlet_pro_elec_2068_version_5]
if exist "C:\gh\oomp_electrical_extension_lead_uk_socket_6_outlet_pro_elec_2068_version_5\.git" (
    echo   skipping: already cloned at C:\gh\oomp_electrical_extension_lead_uk_socket_6_outlet_pro_elec_2068_version_5
) else if exist "C:\gh\oomp_electrical_extension_lead_uk_socket_6_outlet_pro_elec_2068_version_5" (
    echo   skipping: target folder already exists at C:\gh\oomp_electrical_extension_lead_uk_socket_6_outlet_pro_elec_2068_version_5
) else (
    if not exist "C:\gh" mkdir "C:\gh"
    git clone "https://github.com/oomlout/oomp_electrical_extension_lead_uk_socket_6_outlet_pro_elec_2068_version_5.git" "C:\gh\oomp_electrical_extension_lead_uk_socket_6_outlet_pro_elec_2068_version_5"
)
echo.

echo [oomlout_base_version_5]
if exist "C:\gh\oomlout_base_version_5\.git" (
    echo   skipping: already cloned at C:\gh\oomlout_base_version_5
) else if exist "C:\gh\oomlout_base_version_5" (
    echo   skipping: target folder already exists at C:\gh\oomlout_base_version_5
) else (
    if not exist "C:\gh" mkdir "C:\gh"
    git clone "https://github.com/oomlout/oomlout_base_version_5.git" "C:\gh\oomlout_base_version_5"
)
echo.

echo [oomlout_oobb_version_5]
if exist "C:\gh\oomlout_oobb_version_5\.git" (
    echo   skipping: already cloned at C:\gh\oomlout_oobb_version_5
) else if exist "C:\gh\oomlout_oobb_version_5" (
    echo   skipping: target folder already exists at C:\gh\oomlout_oobb_version_5
) else (
    if not exist "C:\gh" mkdir "C:\gh"
    git clone "https://github.com/oomlout/oomlout_oobb_version_5.git" "C:\gh\oomlout_oobb_version_5"
)
echo.

exit /b 0
