from cocciep.db import db
from datetime import datetime

from cocciep.models.enum_gender import EnumGender

class Student(db.Model):
  __tablename__ = 'student'
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  gender_id = db.Column(db.Enum(EnumGender))
  gender_other = db.Column(db.String(128))
  birthdate = db.Column(db.Date(), nullable=False)
  mobile = db.Column(db.String(15), nullable=False)
  mobile2 = db.Column(db.String(15))
  email = db.Column(db.String(128))
  photo = db.Column(db.String(128))
  created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
  deleted_at = db.Column(db.DateTime(), nullable=True)
  student_class = db.relationship('StudentsClassStudents', backref='student', lazy=True)
  grades = db.relationship('Grades', backref='student', lazy=True)
  presence = db.relationship('Presence', backref='student', lazy=True)
