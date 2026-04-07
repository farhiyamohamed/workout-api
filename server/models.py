from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Workout(db.Model):
    __tablename__ = 'workouts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    exercises = db.relationship('WorkoutExercise', back_populates='workout')

class Exercise(db.Model):
    __tablename__ = 'exercises'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    workouts = db.relationship('WorkoutExercise', back_populates='exercise')

class WorkoutExercise(db.Model):
    __tablename__ = 'workout_exercises'
    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))

    workout = db.relationship('Workout', back_populates='exercises')
    exercise = db.relationship('Exercise', back_populates='workouts')