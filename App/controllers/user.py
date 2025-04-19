from App.models import *
from App.database import db

def create_student(username, email, password, first_name, last_name):
    student = Student(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
    db.session.add(student)
    db.session.commit()
    return student

def create_company(username, email, password, company_name):
    company = Company(username=username, email=email, password=password, company_name=company_name)
    db.session.add(company)
    db.session.commit()
    return company

def create_staff(username, email, password, position):
    staff = Staff(username=username, email=email, password=password, position=position)
    db.session.add(staff)
    db.session.commit()
    return staff

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
    