from .user import User
from App.database import db

class Internship(User):

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    company = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, description, company, location, start_date, end_date, user: User):
        self.title = title
        self.description = description
        self.company = company
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.user = user

    def __repr__(self):
        return f"Internship(title={self.title}, company={self.company}, user={self.user.username})"