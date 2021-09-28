from cocciep.db import db

ClassesSubjectsTeachers = db.Table('ClassesSubjectsTeachers',
    db.Column('Class_id', db.Integer(), db.ForeignKey('Class.id'), primary_key=True),
    db.Column('Subject_id', db.Integer(), db.ForeignKey('Subject.id'), primary_key=True),
    db.Column('Teacher_id', db.Integer(), db.ForeignKey('Teacher.id'), primary_key=True),
)

