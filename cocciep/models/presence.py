from cocciep.db import db
from datetime import datetime

class Presence(db.Model):
    __tablename__ = 'presence'
    id = db.Column(db.Integer(), primary_key=True)
    student_id = db.Column(db.Integer(), db.ForeignKey('student.id'), nullable=False) #Create relationship
    present = db.Column(db.Boolean(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    deleted_at = db.Column(db.DateTime(), nullable=True)


