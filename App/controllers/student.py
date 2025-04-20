from App.models import Student, Internship, Application
from App import db

<<<<<<< HEAD
def applyTointernship(internship, student, degree, gpa, graduation_year, resume_url):
    application = Application(internship=internship,
                              student=student,
                                degree=degree, 
                                gpa=gpa,
                                graduation_year=graduation_year,
                                resume_url=resume_url)
    db.session.add(application)
    db.session.commit()
    return application

def get_available_internships():
    return Internship.query.all()

def get_student_applications(student_id):
    return Application.query.filter_by(student_id=student_id).all()

=======
def apply_internship(student_id, internship_id):
    student = Student.query.get(student_id)
    if student:
        student.internship_id = internship_id
        db.session.commit()
        return True
    return False
>>>>>>> 0941f3955f92ad6ffaecdb05564aa457c9175c40
