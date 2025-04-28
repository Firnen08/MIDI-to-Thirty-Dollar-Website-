@echo off

echo [INFO] Installing required Python packages...
REM Install requirements
pip install -r src\requirements.txt

echo [INFO] Launching the MIDI to TDW GUI...
REM Run the GUI
python src\main.py --gui

REM GUI Closed Message
echo.
echo [INFO] GUI closed. Press any key to exit.
pause >nul
