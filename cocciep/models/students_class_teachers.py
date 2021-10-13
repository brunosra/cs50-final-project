from cocciep.db import db
from cocciep.models.enum_subjects import EnumSubjects

class StudentsClassTeachers(db.Model):
    __tablename__ = 'students_class_teachers'
    id = db.Column(db.Integer(), primary_key=True)
    student_class_id = db.Column(db.Integer(), db.ForeignKey('students_class.id'), nullable=False)
    subject = db.Column(db.Enum(EnumSubjects))
    teacher_id = db.Column(db.Integer(), db.ForeignKey('teacher.id'), nullable=False)
    grades = db.relationship('grades', backref='studentsclassteachers', lazy=True)
    
