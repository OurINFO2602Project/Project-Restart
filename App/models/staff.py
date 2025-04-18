from .user import User
from App.models import applicants
from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Staff(User):

    """Staff model."""
    __tablename__ = 'staff'
 
    position = db.Column(db.String(50), nullable=False)


    def __init__(self, name, email, position):
        super().__init__(name, email,)
        self.position = position

    def __str__(self):
        return f"Staff: {self.name}, Position: {self.position}"
    def get_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'position': self.position
        }
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)


