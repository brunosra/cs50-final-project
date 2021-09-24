from cocciep.db import db
from datetime import datetime

class EnumSubjects(db.Model):
  __tablename__ = 'enum_subjects'
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
  deleted_at = db.Column(db.DateTime(), nullable=True)

"""
Seed the enum type:
  matematica
  portugues
  historia
  geografia
  ingles
  desenho_tecnico
  educacao_fisica
  biologia
  fisica
  quimica
  espanhol
  educacao_artistica
  ciencias
"""