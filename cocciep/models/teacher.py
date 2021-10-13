from cocciep.db import db
from datetime import datetime
from cocciep.models.enum_gender import EnumGender

class Teacher(db.Model):
  __tablename__ = 'teacher'
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  gender_id = db.Column(db.Enum(EnumGender))
  gender_other = db.Column(db.String(128), nullable=True)
  birthdate = db.Column(db.Date(), nullable=False)
  mobile = db.Column(db.String(15), nullable=False)
  mobile2 = db.Column(db.String(15))
  email = db.Column(db.String(128), nullable=False, unique=True)
  password_hash = db.Column(db.String(218), nullable=False)
  active = db.Column(db.Boolean(), nullable=False)
  teacher_level = db.Column(db.Integer(), nullable=False, default=1) #1 = teacher | 0=admin
  created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
  deleted_at = db.Column(db.DateTime(), nullable=True)
  classes_subjects_teachers = db.relationship('classessubjectsteachers', backref='teacher', lazy=True)
