Demo Full-Stack Application with Django and REST framework
Overview
This project showcases a full-stack application built using Django and Django REST framework. Key features include user authentication, CRUD operations on tweets, and handling of images and text. The application utilizes Django's ORM and Django REST framework to create a robust RESTful API for tweet management.

Django Tweet App Admin Pannel

Technologies Used
Backend: Django, Django REST framework
Frontend: HTML, minimal CSS, BootStrap
Database: SQLite (default with Django)
Features Implemented
User Authentication:
Users can register and log in.
Basic form validation and password hashing.
Tweet Management:
CRUD operations on tweets (Create, Read, Update, Delete).
Tweets stored with associated user information using Django's ORM.
Image and Text Manipulation:
Upload images along with tweets.
Basic text manipulation (e.g., filtering, basic HTML handling).
Responsive Design:
Minimal CSS for basic responsiveness.
How to Run the Project
Prerequisites
Python 3.x installed locally
Git installed locally
Basic understanding of Django and Django REST framework
Steps to Run
Clone the repository:
git clone https://github.com/Varunv003/django_app
cd django_app
Setup Virtual Environment (Optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:
pip install -r requirements.txt
Apply migrations::
python manage.py migrate
Create a superuser (for admin access):
python manage.py createsuperuser
Run the development server:
python manage.py runserver
Run the development server: Open your web browser and go to http://localhost:8000/
