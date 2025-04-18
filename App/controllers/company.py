from App.models import Company
from App.database import db

def create_internship(company_id, internship_data):
    company = Company.query.get(company_id)
    if company:
        internship = Internship(internship_data)
        company.internships.append(internship)
        db.session.add(internship)
        db.session.commit()
        return internship
    return None

def Internship(internship_data):
    from App.models import Internship  # Import the Internship model

    # Create an internship object using the provided data
    internship = Internship(internship_data)
    return internship


def view_applicants(internship_id):
    from App.models import Internship  # Import the Internship model

    internship = Internship.query.get(internship_id)
    if internship:
        return internship.applicants  # Assuming `applicants` is a relationship in the Internship model
    return None
