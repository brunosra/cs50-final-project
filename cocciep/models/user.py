from cocciep.db import db
from datetime import datetime

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  gender = db.Column(db.String(1)) #M, F, O
  gender_other = db.Column(db.String(128))
  birthdate = db.Column(db.Date(), nullable=False)
  mobile = db.Column(db.String(15), nullable=False)
  mobile2 = db.Column(db.String(15))
  email = db.Column(db.String(128), nullable=False, unique=True)
  password_hash = db.Column(db.String(218), nullable=False)
  active = db.Column(db.Boolean(), nullable=False)
  user_level = db.Column(db.Integer(), nullable=False, default=1) #1 = teacher | 0=admin
  created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
  deleted_at = db.Column(db.DateTime(), nullable=True)