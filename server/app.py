from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from server.models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workout.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Import models so Flask-Migrate can detect tables
from flask import jsonify
from server.models import Workout, Exercise, WorkoutExercise

@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = Workout.query.all()
    return jsonify([{'id': w.id, 'name': w.name} for w in workouts])

@app.route('/exercises', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()
    return jsonify([{'id': e.id, 'name': e.name} for e in exercises])

@app.route('/workouts/<int:workout_id>/exercises', methods=['GET'])
def get_workout_exercises(workout_id):
    we = WorkoutExercise.query.filter_by(workout_id=workout_id).all()
    return jsonify([{'exercise_id': x.exercise_id, 'exercise_name': x.exercise.name} for x in we])

# Example route
@app.route('/')
def home():
    return "Workout API is running!"