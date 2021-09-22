from cocciep.db import db
from datetime import datetime

class Subject(db.Model):
  __tablename__ = 'subject'
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(128))
  created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
  deleted_at = db.Column(db.DateTime(), nullable=True)

# how to create seed automatically  