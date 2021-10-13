from cocciep.db import db
from datetime import datetime
import enum
class EnumGender(enum.Enum):
  MALE = 'male',
  FEMALE = 'female',
  OTHER = 'other',

# class EnumGender(db.Model):
#   __tablename__ = 'enum_gender'
#   id = db.Column(db.Integer(), primary_key=True)
#   name = db.Column(db.String(128), nullable=False)
#   created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
#   deleted_at = db.Column(db.DateTime(), nullable=True)
#   teachers = db.relationship('Teacher', backref='gender', lazy=True)
#   students = db.relationship('Student', backref='gender', lazy=True)
"""
Seed the enum type:
male, female, other
"""
