from cocciep.db import db
from datetime import datetime

class Class(db.Model):
  __tablename__ = 'classes'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), unique=True)
  school_year_id = db.Column(db.Integer(), db.ForeignKey('schoolyears.id'), nullable=False) # create relationship
  status_class_id = db.Column(db.Integer(), db.ForeignKey('statusclasses.id'), nullable=False) # create relationship
  created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
  deleted_at = db.Column(db.DateTime(), nullable=True)

# how to create seed automatically  
