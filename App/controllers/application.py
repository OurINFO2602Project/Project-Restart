from App.models import Application
from App import db

def create_application(internship_id, name, email, degree, gpa, graduation_year, resume_url):
    application = Application(
        internship_id=internship_id,
        name=name,
        email=email,
        degree=degree,
        gpa=gpa,
        graduation_year=graduation_year,
        resume_url=resume_url
    )
    db.session.add(application)
    db.session.commit()
    return application
