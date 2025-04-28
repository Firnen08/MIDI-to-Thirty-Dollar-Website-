@echo off

echo [INFO] Installing required Python packages...
REM Install requirements
pip install -r src\requirements.txt

echo [INFO] Launching the MIDI to TDW GUI...
REM Run the Application
python src\main.py