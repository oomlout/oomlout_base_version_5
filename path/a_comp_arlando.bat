start python C:\gh\oomlout_base_webserver_flask_template_oomp\working_web_oomp.py 
start python C:\od\OneDrive\docs\ai_image_trace_server\run_server.bat

REM ollama section

REM start a_comp_arlando_ollama.bat

REM start a_comp_arlando_webui.bat

REM start open-webui serve
REM start powershell -NoExit -Command "cd 'C:\od\OneDrive\docs\ai_agent_claude_code_local\test_app_1\glm-4.7-flashq4_K_M'; ollama launch claude --model glm-4.7-flash:q4_K_M -- --dangerously-skip-permissions"

REM start python "c:\od\OneDrive\docs\ai_llm_inference_ollama\proxy\app.py"    
REM start explorer "C:\od\OneDrive\docs\ai_llm_inference_ollama\proxy"

REM launch open hardware monitor to keep an eye on GPU usage and then continue
start "" "C:\Program Files (x86)\openhardwaremonitor\OpenHardwareMonitor.exe"

REM launch a cmd with ollama ps run once and leave it open to monitor the Ollama processes anmd then echo ommala ps after it is run
REM start cmd /k "ollama ps & echo Ollama processes listed above. This window will remain open for monitoring. Close it when done."
REM close launcher window
exit