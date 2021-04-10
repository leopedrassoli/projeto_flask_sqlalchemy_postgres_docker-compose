from models import *
import database

#-------------- USER --------------
# POST
def add_user(data):
    db = database.SessionLocal()
    user = User(data['name'], data['email'])
    db.add(user)
    db.commit()
    db.close()
    return None

# GET
def get_user(data):
    db = database.SessionLocal()
    user = User.query.filter_by(name=data['name']).first()
    db.close()
    if user is None:
        return {'status': 'User nao encontrado'}
    return {'user': str(user)}

def get_users():
    db = database.SessionLocal()
    users = User.query.all()
    db.close()
    temp = []
    for u in users:
        jsonUser = {'user':str(u)}
        temp.append(jsonUser)
    return temp

# DELETE
def delete_user(data):
    db = database.SessionLocal()
    user = User.query.filter_by(name=data['name']).first()
    current_db_sessions = db.object_session(user)
    current_db_sessions.delete(user)
    current_db_sessions.commit()
    current_db_sessions.close()
    return None

# PUT
def edit_user(data):
    db = database.SessionLocal()
    for i in data:
        if i == 'email':
            db.execute("UPDATE Users SET email = '" + data['email'] + "' WHERE name='" + data['name'] + "'")
    db.commit()
    db.close()


#-------------- COURSE --------------
# POST
def add_course(data):
    db = database.SessionLocal()
    course = Course(data['description'])
    db.add(course)
    db.commit()
    db.close()
    return None

# GET
def get_course(data):
    db = database.SessionLocal()
    course = Course.query.filter_by(description=data['description']).first()
    db.close()
    if course is None:
        return {'status': 'Course nao encontrado'}
    return {'course': str(course)}

def get_courses():
    db = database.SessionLocal()
    courses = Course.query.all()
    db.close()
    temp = []
    for c in courses:
        jsonUser = {'course':str(c)}
        temp.append(jsonUser)
    return temp

#DELETE
def delete_course(data):
    db = database.SessionLocal()
    course = Course.query.filter_by(description=data['description']).first()
    current_db_sessions = db.object_session(course)
    current_db_sessions.delete(course)
    current_db_sessions.commit()
    current_db_sessions.close()
    return None

# PUT
def edit_course(data):
    db = database.SessionLocal()
    for i in data:
        if i == 'description':
            db.execute("UPDATE Courses SET description = '" + data['description'] + "' WHERE id='" + data['id'] + "'")
    db.commit()
    db.close()


#-------------- GRADE --------------
# POST
def add_grade(data):
    db = database.SessionLocal()
    grade = Grade(data['idUser'], data['idCourse'], data['grade'])
    db.add(grade)
    db.commit()
    db.close()
    return None

# GET
def get_grade(data):
    db = database.SessionLocal()
    grade = Grade.query.filter_by(idUser=data['idUser'], idCourse=data['idCourse']).first()
    db.close()
    if grade is None:
        return {'status': 'Grade nao encontrada'}
    return {'grade': str(grade)}

def get_grades():
    db = database.SessionLocal()
    grades = Grade.query.all()
    db.close()
    temp = []
    for g in grades:
        jsonUser = {'grade':str(g)}
        temp.append(jsonUser)
    return temp

# DELETE
def delete_grade(data):
    db = database.SessionLocal()
    grade = Grade.query.filter_by(idUser=data['idUser'], idCourse=data['idCourse']).first()
    current_db_sessions = db.object_session(grade)
    current_db_sessions.delete(grade)
    current_db_sessions.commit()
    current_db_sessions.close()
    return None

#-------------- REPORT --------------
# GET
def get_report():
    db = database.SessionLocal()
    grades = Grade.query.all()
    db.close()
    temp = []
    for g in grades:
        jsonUser = {'User':g.user.name, 'Course':g.course.description, 'Grade':g.grade}
        temp.append(jsonUser)
    return temp