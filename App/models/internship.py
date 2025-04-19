from App.database import db

class Internship(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), nullable=False)
  description = db.Column(db.String(120), nullable=False)
  start_date = db.Column(db.String(20), nullable=False)
  end_date = db.Column(db.String(20), nullable=False)
  salary = db.Column(db.Integer, nullable=False)
  company_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  company = db.relationship('Company', backref=db.backref('internships', lazy=True))

  def __init__(self, title, description, start_date, end_date, salary):
    self.title = title
    self.description = description
    self.start_date = start_date
    self.end_date = end_date
    self.salary = salary
    
  def get_json(self):
    return {
        "id": self.id,
        "title": self.title,
        "start date": self.start_date,
        "end date": self.end_date,
        "description": self.description,
        "salary": self.salary,
    }
