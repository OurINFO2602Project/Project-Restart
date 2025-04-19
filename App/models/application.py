from App.database import db

class Application(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  internship_id = db.Column(db.Integer, db.ForeignKey('internship.id'), nullable=False)
  student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  status = db.Column(db.String(80), nullable=False, default='pending')
  degree = db.Column(db.String(120), nullable=False)
  gpa = db.Column(db.Float, nullable=False)
  graduation_year = db.Column(db.Integer, nullable=False)
  resume_url = db.Column(db.String(120), nullable=False)
  student = db.relationship('Student', backref=db.backref('applications', lazy=True))
  internship = db.relationship('Internship', backref=db.backref('applications', lazy=True))

  def __init__(self, internship, student, degree, gpa, graduation_year, url="https://file.pdf"):
    self.internship = internship
    self.student = student
    self.degree = degree
    self.gpa = gpa
    self.graduation_year = graduation_year
    self.resume_url =  url

  def get_json(self):
    return {
        "id": self.id,
        "internship_id": self.internship_id,
        "internship": self.internship.title,
        "student_id": self.student_id,
        "student": self.student.username,
        "degree": self.degree,
        "gpa": self.gpa,
        "graduation_year": self.graduation_year,
        "status": self.status,
        "resume_url": self.resume_url
    }
