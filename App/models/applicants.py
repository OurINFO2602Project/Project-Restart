from .student import Students
from App.database import db

class Applicants(Students):
    super().__init__()
    def __init__(self, name, email, password, resume):
        super().__init__(name, email, password)
        self.resume = resume
        self.role = 'applicant'
        applicant_id = self.id

    __tablename__ = 'applicants'
    id = db.Column(db.Integer, db.ForeignKey('applicant.id'), primary_key=True)
    name = db.Column(db.String(50), nullable=False)