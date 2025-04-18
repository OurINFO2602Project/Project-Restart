from .user import User
from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Company(User):

    company_name = db.Column(db.String(80), nullable=False)


    """Company model."""
    __tablename__ = 'companies'

    def __init__(self, name, email, password, company_name):
        super().__init__(name, email, password)
        self.company_name = company_name

    def __str__(self):
        return f"Company: {self.company_name}, Email: {self.email}"
    def get_json(self):
        return{
            'id': self.id,
            'username': self.username,
            'company_name': self.company_name
        }
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
   