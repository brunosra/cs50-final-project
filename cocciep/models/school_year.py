from cocciep.db import db
from datetime import datetime

class SchoolYear(db.Model):
  __tablename__ = 'schoolyear'
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  start = db.Column(db.Date(), nullable=False)
  end = db.Column(db.Date(), nullable=False)
  picture = db.Column(db.String(128))
  created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
  deleted_at = db.Column(db.DateTime(), nullable=True)
