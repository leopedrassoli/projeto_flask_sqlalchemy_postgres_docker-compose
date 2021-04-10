from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email
    
    def __repr__(self):
        return 'User ' + str(self.id) + ", " + self.name + ", " + self.email


class Course(Base):
    __tablename__ = "Courses"

    id = Column(Integer, primary_key=True)
    description = Column(String(50), unique=True)

    def __init__(self, description=None):
        self.description = description
    
    def __repr__(self):
        return 'Course ' + str(self.id) + ", " + self.description


class Grade(Base):
    __tablename__ = "Grades"

    id = Column(Integer, primary_key=True)
    idUser = Column(Integer, ForeignKey(User.id))
    idCourse = Column(Integer, ForeignKey(Course.id))
    grade = Column(Integer)

    user = relationship('User', foreign_keys='Grade.idUser')
    course = relationship('Course', foreign_keys='Grade.idCourse')

    def __init__(self, idUser=None, idCourse=None, grade=None):
        self.idUser = idUser
        self.idCourse = idCourse
        self.grade = grade
    
    def __repr__(self):
        return 'Grade ' + str(self.id) + ", idUser: " + str(self.idUser) + ", idCourse: " + str(self.idCourse) + ":" + str(self.grade)

