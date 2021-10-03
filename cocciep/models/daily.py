from cocciep.db import db
from datetime import datetime

from cocciep.models.enum_status_class import EnumStatusClass

class Daily(db.Model):
    __tablename__ = 'dailies'
    id = db.Column(db.Integer(), primary_key=True),
    class_id = db.Column(db.Integer(), db.ForeignKey('StudentsClass.id'), nullable=False) #Create relationship
    subject_id = db.Column(db.Integer(), db.ForeignKey('Subject.id'), nullable=False) #Create relationship
    status = db.Column(db.Enum(EnumStatusClass))
    date = db.Column(db.DateTime(), nullable=False, default=datetime.now().date())
    content = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    deleted_at = db.Column(db.DateTime(), nullable=True)
    
