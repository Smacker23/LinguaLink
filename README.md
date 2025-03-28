A Django and React-based website designed to assist with language learning. It utilizes a flashcard system to help users effectively memorize vocabulary and key concepts.

1️⃣ Prerequisites
Ensure you have the following installed on your system:

Python 3

Node.js & npm

Git (optional)

2️⃣ Setting Up the Project
You can easily set up the project by running the provided script:

Windows:
Run the batch script setup_django.bat:

batch
Copy
Edit
@echo off
cd /d "backend"
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
Create a .env file inside the frontend folder.

Inside the .env file, define the base API URL variable as:

ini
Copy
Edit
REACT_APP_BASE_API_URL=<your_api_url>
Open backend/lingualink/settings.py and configure your database settings.

3️⃣ Running the Project
Windows:
Run the batch script run.bat:

batch
Copy
Edit
@echo off
cd /d "backend"
start cmd /k "venv\Scripts\activate && python manage.py runserver"

cd /d "../frontend"
start cmd /k "npm start"
