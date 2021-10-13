from cocciep.db import db
from datetime import datetime
from cocciep.models.enum_bimester import EnumBimester

class Grades(db.Model):
    __tablename__ = 'grade'
    id = db.Column(db.Integer(), primary_key=True)
    student_id = db.Column(db.Integer(), db.ForeignKey('student.id'), nullable=False)
    classes_subjects_teachers_id = db.Column(db.Integer(), db.ForeignKey('students_class_teachers.id'), nullable=False)
    bimester = db.Column(db.Enum(EnumBimester))
    grade = db.Column(db.Float(), nullable=True)
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    deleted_at = db.Column(db.DateTime(), nullable=True)