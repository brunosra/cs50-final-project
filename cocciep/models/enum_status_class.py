from cocciep.db import db
from datetime import datetime

class EnumStatusClass(db.Model):
  __tablename__ = 'enum_statusclass'
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
  deleted_at = db.Column(db.DateTime(), nullable=True)
  dailies = db.relationship('Daily', backref=status, lazy=True) # Many-to-one relationship (One status can be in many dailies, but one daily only can have one status)

"""
Seed the enum type:
active, finished, cancelled 
"""
