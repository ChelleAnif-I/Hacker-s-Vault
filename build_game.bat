@echo off
cd /d "%~dp0"

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m PyInstaller --onefile --name HackerVault hackers_vault.py

echo.
echo Build finished. Your executable is in the dist folder.
pause
