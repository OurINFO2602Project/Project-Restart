from App.models import Staff
from App import db
from App.models import Application, shortlist

def get_pending_applications():
    return Application.query.filter_by().all()

def shortlist_student(internship_id, student_id, staff_id):
        application = Application.query.filter_by(
            internship_id=internship_id, 
            student_id=student_id).first()
        if application:
            application.status = 'shortlisted'
            db.session.add(application)

        shortlisted = shortlist(
            internship_id=internship_id, 
            student_id=student_id, 
            staff_id=staff_id
        )
        db.session.add(shortlisted)
        db.session.commit()
        return True
    return False

def get_all_shortlists():
     return shortlist.query.all()
