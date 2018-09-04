from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
class Grade(db.Model):
    __tablename__='grade'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    g_name=db.Column(db.String(20))
    g_students=db.relationship('Student',backref='grade',lazy=True)

class Student(db.Model):
    __tablename__='student'
    id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    name=db.Column(db.String(30))
    age=db.Column(db.Integer)
    score=db.Column(db.FLOAT,nullable=False)
    s_grade=db.Column(db.Integer,db.ForeignKey('grade.id'))