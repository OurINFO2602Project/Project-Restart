from .user import User
from App.database import db

class Company(User):
  __tablename__ = 'company'
  __mapper_args__ = {
      'polymorphic_identity': 'company',
  }
  
  company_name = db.Column(db.String(120), nullable=False)

  def __init__(self, username, email, password, company_name):
    super().__init__(username, email, password)
    self.company_name = company_name
