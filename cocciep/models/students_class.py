from cocciep.db import db
from datetime import datetime
import enum

from cocciep.models.enum_status_class import EnumStatusClass

class StudentsClass(db.Model):
  __tablename__ = 'students_class'
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(128), unique=True)
  school_year_id = db.Column(db.Integer(), db.ForeignKey('schoolyear.id'), nullable=False)
  status_class_id = db.Column(db.Enum(EnumStatusClass))
  created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
  deleted_at = db.Column(db.DateTime(), nullable=True)
  students_classes_students = db.relationship('StudentsClassStudents', backref='studentsclass', lazy=True)
  student_class = db.relationship('studentsclassteachers', backref='studentsclass', lazy=True)

# how to create seed automatically  
