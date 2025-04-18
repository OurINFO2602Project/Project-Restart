from .user import User
from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db


class Student(User):

    degree = db.Column(db.String(50), nullable=True)
    gpa = db.Column(db.Float, nullable=True)
    graduation_year = db.Column(db.Integer, nullable=True)


    """Student model."""
    __tablename__ = 'students'

    def __init__(self, username, password):
        super().__init__(username, password)
        self.role = 'student'
        self.set_password(password)

    def get_json(self):
        """Get JSON representation of the student."""
        return {
            'id': self.id,
            'username': self.username,
            'role': self.role

        }
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
    def __repr__(self):
        return f'<Student {self.username}>'