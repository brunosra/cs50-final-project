import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from cocciep.db import db

from cocciep.models.teacher import Teacher

# Models
from cocciep.models.teacher import Teacher
from cocciep.models.students_class import StudentsClass
from cocciep.models.students_class_students import StudentsClassStudents
from cocciep.models.student import Student
from cocciep.models.school_year import SchoolYear
from cocciep.models.presence import Presence
from cocciep.models.grades import Grades
from cocciep.models.enum_subjects import EnumSubjects
from cocciep.models.enum_status_class import EnumStatusClass
from cocciep.models.enum_gender import EnumGender
from cocciep.models.enum_bimester import EnumBimester

from cocciep.models.students_class_teachers import StudentsClassTeachers


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
  
  # importing blueprints
  from cocciep.blueprints.auth import bp
  # from cocciep.blueprints.subjects import bp
  app.register_blueprint(bp)

  return app
