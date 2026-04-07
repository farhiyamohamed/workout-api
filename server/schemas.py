from marshmallow import Schema, fields

class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int()
    exercise_id = fields.Int()