from App.models import Staff
from App import db
from App.models import applicants

def view_applicants():
    applicants = applicants.query.all()
    return applicants

def view_applicant(applicant_id):
    applicant = applicants.query.filter_by(id=applicant_id).first()
    if not applicant:
        return None
    return applicant

def approve_applicant(applicant_id):
    applicant = applicants.query.filter_by(id=applicant_id).first()
    if not applicant:
        return None
    applicant.status = 'approved'
    db.session.commit()
    return applicant