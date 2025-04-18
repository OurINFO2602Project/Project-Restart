from App.models import Student
from App import db

def applyTointernship(student_id, internship_id):
    student = Student.query.get(student_id)
    if student:
        student.internship_id = internship_id
        db.session.commit()
        return True
    return False