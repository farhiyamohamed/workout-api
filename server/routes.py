from flask import request, jsonify
from .models import db, Exercise, Workout, WorkoutExercise
from datetime import datetime

def register_routes(app):

    # ---------------- EXERCISES ----------------
    @app.route("/exercises", methods=["GET"])
    def get_exercises():
        exercises = Exercise.query.all()
        return jsonify([{
            "id": e.id,
            "name": e.name,
            "category": e.category,
            "equipment_needed": e.equipment_needed
        } for e in exercises])

    @app.route("/exercises/<int:id>", methods=["GET"])
    def get_exercise(id):
        e = Exercise.query.get_or_404(id)
        return jsonify({
            "id": e.id,
            "name": e.name,
            "category": e.category,
            "equipment_needed": e.equipment_needed,
            "workouts": [{"id": we.workout.id, "date": str(we.workout.date)} for we in e.workout_exercises]
        })

    @app.route("/exercises", methods=["POST"])
    def create_exercise():
        data = request.json
        try:
            e = Exercise(
                name=data.get("name"),
                category=data.get("category"),
                equipment_needed=data.get("equipment_needed", False)
            )
            db.session.add(e)
            db.session.commit()
        except Exception as ex:
            db.session.rollback()
            return {"error": str(ex)}, 400
        return {"message": "Exercise created", "id": e.id}, 201

    @app.route("/exercises/<int:id>", methods=["DELETE"])
    def delete_exercise(id):
        e = Exercise.query.get_or_404(id)
        db.session.delete(e)
        db.session.commit()
        return {"message": "Exercise deleted"}

    # ---------------- WORKOUTS ----------------
    @app.route("/workouts", methods=["GET"])
    def get_workouts():
        workouts = Workout.query.all()
        return jsonify([{
            "id": w.id,
            "date": str(w.date),
            "duration_minutes": w.duration_minutes,
            "notes": w.notes
        } for w in workouts])

    @app.route("/workouts/<int:id>", methods=["GET"])
    def get_workout(id):
        w = Workout.query.get_or_404(id)
        return jsonify({
            "id": w.id,
            "date": str(w.date),
            "duration_minutes": w.duration_minutes,
            "notes": w.notes,
            "exercises": [{
                "exercise_id": we.exercise.id,
                "name": we.exercise.name,
                "reps": we.reps,
                "sets": we.sets,
                "duration_seconds": we.duration_seconds
            } for we in w.workout_exercises]
        })

    @app.route("/workouts", methods=["POST"])
    def create_workout():
        data = request.json
        try:
            w = Workout(
                date=datetime.strptime(data.get("date"), "%Y-%m-%d").date(),
                duration_minutes=data.get("duration_minutes"),
                notes=data.get("notes")
            )
            db.session.add(w)
            db.session.commit()
        except Exception as ex:
            db.session.rollback()
            return {"error": str(ex)}, 400
        return {"message": "Workout created", "id": w.id}, 201

    @app.route("/workouts/<int:id>", methods=["DELETE"])
    def delete_workout(id):
        w = Workout.query.get_or_404(id)
        db.session.delete(w)
        db.session.commit()
        return {"message": "Workout deleted"}

    # ---------------- WORKOUT-EXERCISE ----------------
    @app.route("/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises", methods=["POST"])
    def add_exercise_to_workout(workout_id, exercise_id):
        data = request.json
        we = WorkoutExercise(
            workout_id=workout_id,
            exercise_id=exercise_id,
            reps=data.get("reps"),
            sets=data.get("sets"),
            duration_seconds=data.get("duration_seconds")
        )
        db.session.add(we)
        db.session.commit()
        return {"message": "Exercise added to workout", "id": we.id}, 201