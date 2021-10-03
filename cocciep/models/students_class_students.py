from cocciep.db import db
from datetime import datetime

class StudentsClassStudents(db.Model):
  __tablename__ = 'students_class_students'
  id = db.Column(db.Integer(), primary_key=True)
  student_id = db.Column(db.Integer(), db.ForeignKey('student.id'), nullable=False) # create relationship
  students_class_id = db.Column(db.Integer(), db.ForeignKey('students_class.id'), nullable=False) # create relationship
  created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
  deleted_at = db.Column(db.DateTime(), nullable=True)

# how to create seed automatically  
