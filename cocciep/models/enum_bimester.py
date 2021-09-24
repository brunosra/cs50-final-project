from cocciep.db import db
from datetime import datetime

class EnumBimester(db.Model):
  __tablename__ = 'enum_bimester'
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
  deleted_at = db.Column(db.DateTime(), nullable=True)

"""
Seed the enum type:
  1
  2
  3
  4
"""