from .user import create_student, create_company, create_staff
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    create_student('bob', 'bob@email.com', 'bobpass', 'Bob', 'Smith')
    create_company('pam', 'randy@email.com', 'pampass', 'Company1')
    create_staff('rob', 'rob@email.com', 'robpass', 'lecturer')
