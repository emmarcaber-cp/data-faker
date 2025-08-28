@echo off
REM Change to the project directory
cd /d "C:\Users\Owner\Personal\data-faker"
call venv\Scripts\activate
REM Build the Data Faker App as a Windows executable using PyInstaller
pyinstaller --onefile --noconsole --icon=app_icon.ico data_faker_app.py

echo.
echo Build complete! Your executable is in the dist folder.
pause
