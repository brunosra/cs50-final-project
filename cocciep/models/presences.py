from cocciep.db import db
from datetime import datetime

class Presence(Model.db):
    __tablename__ = 'presences'
    id = db.Column(db.Integer(), primary_key=True),
    daily_id = db.Column(db.Integer(), db.ForeignKey('Daily.id'), nullable=False) #Create relationship
    student_id = db.Column(db.Integer(), db.ForeignKey('Student.id'), nullable=False) #Create relationship
    present = db.Column(db.Boolean(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    deleted_at = db.Column(db.DateTime(), nullable=True)


