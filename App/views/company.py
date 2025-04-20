from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from App.controllers.company import *
from App.models.internship import Internship
from App.models.shortlist import Shortlist
from App.models.student import Student

company_blueprint = Blueprint('company', __name__)

@company_blueprint.route('/home', methods=['GET'])
@login_required
def home():
 if current_user.role != 'company':
  flash('Access denied.')
  return redirect(url_for('auth.login'))
 
 internships = App.controllers.company.get_company_internships(current_user.id)
 return render_template('company1stpage.html', internships=internships, company = current_user)

@company_blueprint.route('/internship/<int:internship_id>/shortlist')
@login_required
def view_shortlist(internship_id):
 if current_user.role != 'company':
  flash('Access denied.')
  return redirect(url_for('auth.login'))
 
 internship = Internship.query.get(internship_id)
 if not internship or internship.company_id != current_user.id:
  flash('Internship not found')
  return redirect(url_for('company.home'))
 
 shortlisted = Shortlist.query.filter_by(internship_id=internship_id).all()
 selected_student_id = request.args.get('selected')
 selected_student = Student.query.get(selected_student_id) if selected_student_id else None

 return render_template('company_shortlist.html',
                        internship=internship,
                        shortlisted_students=shortlisted,
                        selected_student=selected_student)

@company_blueprint.route('/api/students/<int:student_id>')
@login_required
def get_student_details(student_id):
    if current_user.role != 'company':
        return {'error': 'Access denied'}, 403
    
    student = Student.query.get(student_id)
    if not student:
        return {'error': 'Student not found'}, 404
    
    application = Application.query.filter_by(
        student_id=student_id
    ).first()
    
    return {
        'id': student.id,
        'name': f"{student.first_name} {student.last_name}",
        'email': student.email,
        'degree': application.degree if application else 'N/A',
        'gpa': application.gpa if application else 0.0,
        'graduation_year': application.graduation_year if application else 0,
        'resume_url': application.resume_url if application else ''
    }