from cocciep.db import db
from datetime import datetime

class StudentsClass(db.Model):
  __tablename__ = 'students_class'
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(128), unique=True)
  school_year_id = db.Column(db.Integer(), db.ForeignKey('schoolyear.id'), nullable=False) # create relationship
  status_class_id = db.Column(db.Integer(), db.ForeignKey('enum_statusclass.id'), nullable=False) # create relationship
  created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
  deleted_at = db.Column(db.DateTime(), nullable=True)
  students = db.relationship('Students', backref='students_class', lazy=True)

# how to create seed automatically  
