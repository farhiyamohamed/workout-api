Workout API
A RESTful API for managing workouts, exercises, and workout plans built with Flask, SQLAlchemy, and Flask-Migrate.
Table of Contents
Project Overview
Features
Technologies Used
Installation
Database Setup
Seeding Data
Running the Application
API Endpoints
GitHub Submission
Contributing
License

Project Overview
This project is a simple workout management API designed to:
Track workouts and exercises
Associate exercises with workouts
Seed initial workout and exercise data
Provide a foundation for a fitness app backend

Features
CRUD operations for workouts and exercises
Many-to-many relationship between workouts and exercises
Database migrations using Flask-Migrate
Easy seeding of initial data
Fully RESTful endpoints
Technologies Used
Python 3.9
Flask 3.1
SQLAlchemy 3.0
Flask-Migrate 3.1
SQLite (default development database)

Installation
Clone the repository:
git clone https://github.com/farhiyamohamed/workout-api.git
cd workout-api
Install dependencies using Pipenv:
pipenv install
pipenv shell
Set the Flask application environment:
export FLASK_APP=server.app
Database Setup

Initialize the database and migrations:
python -m flask db init
python -m flask db migrate -m "Initial migration"
python -m flask db upgrade
This will create the SQLite database and tables for workouts and exercises.
Seeding Data
To populate the database with initial data:
python -m server.seed
You should see:
Database seeded successfully!
Running the Application

Start the Flask development server:
python -m flask run
Access the API at:
http://127.0.0.1:5000
API Endpoints
GET /workouts – Retrieve all workouts
GET /exercises – Retrieve all exercises
POST /workouts – Add a new workout
POST /exercises – Add a new exercise
POST /workout_exercises – Associate an exercise with a workout
(You can expand this list with all routes your API supports.)
GitHub Submission
Initialize Git (if not already done):
git init
Add all files:
git add .
Commit changes:
git commit -m "Final submission of Workout API project"
Connect to your GitHub repository:
git remote add origin https://github.com/farhiyamohamed/workout-api.git
Push to GitHub:
git branch -M main
git push -u origin main


