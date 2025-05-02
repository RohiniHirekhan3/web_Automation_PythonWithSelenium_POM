@echo off

REM Step 1: Go to project directory (optional if already there)
cd /d C:\Users\RohiniHirekhan\PycharmProjects\NopCommerce_project

REM Step 2: Activate virtual environment
call .venv\Scripts\activate.bat

REM Step 3: Run tests using python -m pytest
python -m pytest -v -s -m "sanity" --html=Reports\report1.html TestCases/test_Login.py --browser chrome



pause
