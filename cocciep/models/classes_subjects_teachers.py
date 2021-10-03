from cocciep.db import db

class ClassesSubjectsTeachers(db.Model):
    __tablename__ = 'classes_subjects_teachers'
    id = db.Column(db.Integer(), primary_key=True)
    student_class_id = db.Column(db.Integer(), db.ForeignKey('StudentsClass.id'), nullable=False)
    subject_id = db.Column(db.Integer(), db.ForeignKey('Subject.id'), nullable=False)
    teacher_id = db.Column(db.Integer(), db.ForeignKey('Teacher.id'), nullable=False)
