import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from cocciep.db import db

from cocciep.models.teacher import Teacher

# Models
from cocciep.models.teacher import Teacher
from cocciep.models.subject import Subject
from cocciep.models.students_class import StudentsClass
from cocciep.models.students_class_students import StudentsClassStudents
from cocciep.models.student import Student
from cocciep.models.school_year import SchoolYear
from cocciep.models.recuperation_grade_students import RecuperationGradeStudents
from cocciep.models.presences import Presence
from cocciep.models.final_test_grade_students import FinalTestGradeStudents
from cocciep.models.presences import Presence
from cocciep.models.enum_subjects import EnumSubjects
from cocciep.models.enum_status_daily import EnumStatusDaily
from cocciep.models.enum_status_class import EnumStatusClass
from cocciep.models.enum_gender import EnumGender
from cocciep.models.enum_bimester import EnumBimester
from cocciep.models.daily import Daily
# from cocciep.models.classes_subjects_teachers import ClassesSubjectsTeachers
from cocciep.models.bimestral_grades_students import BimestralGradesStudents

def create_app(test_config=None):
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'cocciep.sqlite'),
    SQLALCHEMY_DATABASE_URI='sqlite:///cocciep.sqlite'
  )

  db.init_app(app)
  Migrate(app, db)

  # importing models:
  from cocciep.models.subjects import Subject
  from cocciep.models.teacher import Teacher
  
  # importing blueprints
  from cocciep.blueprints.auth import bp
  from cocciep.blueprints.subjects import bp
  app.register_blueprint(bp)

  return app
