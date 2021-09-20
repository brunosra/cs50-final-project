import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from cocciep.db import db

from cocciep.models.user import User

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
  from cocciep.models.user import User
  
  # importing blueprints
  from cocciep.blueprints.auth import bp
  from cocciep.blueprints.subjects import bp
  app.register_blueprint(bp)

  return app