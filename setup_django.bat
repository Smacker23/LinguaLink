@echo off
cd /d "backend"
python -m venv test
call test\Scripts\activate
pip install -r requirements.txt
