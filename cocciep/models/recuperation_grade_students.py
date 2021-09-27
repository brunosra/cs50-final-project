from cocciep.db import db
from sqlalchemy import Integer, Enum
from datetime import datetime

class BimestralGradesStudents(db.Model):
    id = db.Column(db.Integer(), primary_key=True),
    student_id = db.Column(db.Integer(), ForeignKey('Student'), nullable=False),
    # it is necessary to link it to classes_subjects_teachers model
    grade = db.Column(db.Float(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    deleted_at = db.Column(db.DateTime(), nullable=True)