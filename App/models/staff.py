from .user import User
from App.database import db

class Staff(User):
  __tablename__ = 'staff'
  __mapper_args__ = {
      'polymorphic_identity': 'staff',
  }
  
  position = db.Column(db.String(50), nullable=True)

  def __init__(self, username, email, password, position):
    super().__init__(username, email, password)
    self.position = position
