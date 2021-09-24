from cocciep.db import db
from datetime import datetime

class EnumGender(db.Model):
  __tablename__ = 'enum_gender'
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
  deleted_at = db.Column(db.DateTime(), nullable=True)
  users = db.relationship('User', backref='gender', lazy=True)
"""
Seed the enum type:
male, female, other
"""