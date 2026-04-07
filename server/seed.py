from server.app import app
from server.models import db, Workout, Exercise, WorkoutExercise

with app.app_context():
    db.create_all()

    # Clear existing data
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()
    db.session.commit()

    # Sample data
    w1 = Workout(name="Morning Workout")
    w2 = Workout(name="Evening Workout")

    e1 = Exercise(name="Push Up")
    e2 = Exercise(name="Squat")
    e3 = Exercise(name="Sit Up")

    db.session.add_all([w1, w2, e1, e2, e3])
    db.session.commit()

    we1 = WorkoutExercise(workout_id=w1.id, exercise_id=e1.id)
    we2 = WorkoutExercise(workout_id=w1.id, exercise_id=e2.id)
    we3 = WorkoutExercise(workout_id=w2.id, exercise_id=e2.id)
    we4 = WorkoutExercise(workout_id=w2.id, exercise_id=e3.id)

    db.session.add_all([we1, we2, we3, we4])
    db.session.commit()

    print("Database seeded successfully!")