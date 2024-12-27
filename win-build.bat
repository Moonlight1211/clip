:: Windows installation script for CLIp
:: Please report any issues to https://github.com/Moonlight1211/clip/issues
@echo OFF

:: Virtual environment directory
set venv_dir=lib\venv
:: Options used in PyInstaller operation
set pyinst_opts=-F -n clip --specpath src --distpath . --log-level ERROR

:: If the venv doesn't exist, create one and install all dependencies
if not exist %venv_dir%\ (
    :: Create new Python virtual environment
    python -m venv %venv_dir%
    :: Activate the virtual environment
    call %venv_dir%\Scripts\activate.bat
    :: Install required dependencies
    pip install -q -r lib\requirements.txt
) else (
    :: Venv exists, so just activate the virtual environment
    call %venv_dir%\Scripts\activate.bat
)

:: Run PyInstaller to build program
echo Building...
pyinstaller %pyinst_opts% src\main.py

:: Deactive the virtual environment
call deactivate
:: Clean up build files
rmdir /S /Q build
del src\*.spec
:: Inform user that the operation is done
echo Done!