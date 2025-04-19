from .user import User
from App.database import db

class Student(User):
  __tablename__ = 'student'
  __mapper_args__ = {
      'polymorphic_identity': 'student',
  }
  
  first_name = db.Column(db.String(80), nullable=False)
  last_name = db.Column(db.String(80), nullable=False)

  def __init__(self, username, email, password, first_name, last_name):
    super().__init__(username, email, password)
    self.first_name = first_name
    self.last_name = last_name
