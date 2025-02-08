# LinguaLink
A Django and React-based website designed to assist with language learning. It utilizes a flashcard system to help users effectively memorize vocabulary and key concepts.

### **1️⃣ Prerequisites**
Ensure you have the following installed on your system:
- [Python 3](https://www.python.org/downloads/)
- [Node.js & npm](https://nodejs.org/en/)
- Git (optional)

### **2️⃣ Setting Up the Project**
You can easily set up the project by running the provided script:

#### **Windows:**
1. Run batch script "setup_django.bat
```batch
@echo off
cd /d "backend"
python -m venv venv
call test\Scripts\activate
pip install -r requirements.txt
```
2. Create .env file inside frontend folders
3. Inside .env file add api url, needs to start with `REACT_APP`

### **3️⃣ Run the Project**
#### **Windows:**
1. Run batch script "run.bat
```batch
@echo off
cd /d "backend"
start cmd /k "venv\Scripts\activate && python manage.py runserver"


cd /d "../frontend"
start cmd /k "npm start"

```
