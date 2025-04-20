from App.models import Company, Internship, Application, shortlist  # Import the Company and Internship models
from App.database import db

def create_internship(company_id, title, description, start_date, end_date, salary):
   internship = Internship(title=title,
                           description=description,
                           start_date=start_date,
                           end_date=end_date,
                           salary=salary,
                           company_id=company_id)
   db.session.add(internship)
   db.session.commit()
   return internship
   
def get_company_internships(company_id):
   return Internship.query.filter_by(company_id=company_id).all()

def get_internship_applications(internship_id):
   return Application.query.filter_by(internship_id=internship_id).all()

def get_shortlisted_students(internship_id):
   return shortlist.query.filter_by(internship_id=internship_id).all()