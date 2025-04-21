from App.models import Application, Internship, Student
from App.database import db

def create_application(internship_id, student_id, degree, gpa, graduation_year, resume_url):
    internship = Internship.query.get(internship_id)
    student = Student.query.get(student_id)
    if internship or student:
        application = Application(internship=internship, student=student, degree=degree, gpa=gpa, graduation_year=graduation_year, url=resume_url)
        db.session.add(application)
    db.session.commit()
    return application