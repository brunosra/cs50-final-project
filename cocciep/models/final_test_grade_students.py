from cocciep.db import db
from datetime import datetime

class FinalTestGradeStudents(db.Model):
    id = db.Column(db.Integer(), primary_key=True),
    student_id = db.Column(db.Integer(), db.ForeignKey('Student.id'), nullable=False) #Create relationship
    # How to use Table ClassesSubjectsTeachers if it doesn't have id?
    class_id = db.Column(db.Integer(), db.ForeignKey('StudentsClass.id'), nullable=False) #Create relationship
    subject_id = db.Column(db.Integer(), db.ForeignKey('Subject.id'), nullable=False) #Create relationship
    teacher_id = db.Column(db.Integer(), db.ForeignKey('Teacher.id'), nullable=False) #Create relationship
    grade = db.Column(db.Float(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    deleted_at = db.Column(db.DateTime(), nullable=True)