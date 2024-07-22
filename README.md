# gymalytics-backend
backend for a simple web-app to manage gym sessions and track progress

Create Python Venv
python3 -m venv venv

Switch to Venv
source venv/bin/activate

Install requirements
pip install -r ./requirements.txt 

Create DB Tables
python3 manage.py makemigrations
python3 manage.py migrate

Run dev server
python3 manage.py runserver