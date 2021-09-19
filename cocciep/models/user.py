from cocciep.db import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128))
  password_hash = db.Column(db.String(218))
  user_level = db.Column(db.Integer())