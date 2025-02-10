@echo off
cd /d "backend"
start cmd /k "venv\Scripts\activate && python manage.py runserver"


cd /d "../frontend"
start cmd /k "npm start"
