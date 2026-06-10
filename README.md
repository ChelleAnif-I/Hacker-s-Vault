# Hacker's Vault

Enter the Hacker's Vault. Crack codes, bypass defenses, and uncover hidden secrets in this fast-paced hacking-themed game.

## What you need to run it in VS Code

1. Install Python 3.10 or newer from https://www.python.org/downloads/
2. Open this folder in Visual Studio Code.
3. Open a terminal in the project root.
4. Create and activate a virtual environment:
   - Windows PowerShell:
     - py -m venv .venv
     - .\.venv\Scripts\Activate.ps1
5. Install the project dependencies:
   - python -m pip install --upgrade pip
   - python -m pip install -r requirements.txt
   - or, for an installable package: python -m pip install -e .

## Run the game

- python hackers_vault.py
- or, after installing the package in editable mode:
  - hackers-vault

## Make it downloadable

This project now includes:

- requirements.txt for Python dependencies
- pyproject.toml so the game can be installed with pip
- build_game.bat for a simple Windows EXE build

To create a Windows executable:

1. Make sure the dependencies are installed.
2. Run:
   - py -m PyInstaller --onefile --name HackerVault hackers_vault.py
3. The build output will appear in the dist folder.

You can also run the included batch file:

- build_game.bat

## Notes

The current version is a console-based game. If you want to turn it into a full graphical Pygame game later, the included pygame dependency is already set up for that next step.
