from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from App.controllers.staff import *
from App.models import Application, Student
import App
from App.models.shortlist import Shortlist

staff_blueprint = Blueprint('staff', __name__, url_prefix='/staff')

@staff_blueprint.route('/home')
@login_required
def home():
 if current_user.role != 'staff':
  return redirect(url_for('auth.login'))
 
 applications = App.controller.staff.get_pending_applications()
 applicants = {
  app.id: {
            'id': app.id,
            'name': f"{app.student.first_name} {app.student.last_name}",
            'degree': app.degree,
            'gpa': app.gpa,
            'graduation_year': app.graduation_year,
            'resume_url': app.resume_url,
            'shortlisted': bool(Shortlist.query.filter_by(student_id=app.student_id, internship_id=app.internship_id).first())
        }
        for app in applications
 }

 selected_applicant_id = request.args.get('applicant_id')
 selected_applicant = applicants.get(int(selected_applicant_id)) if selected_applicant_id else None
 return render_template('staff_home.html',
                        applicants = applicants,
                        selected_applicants=selected_applicant)

@staff_blueprint.route('/applicant/<int:applicant_id>/shortlist')
@login_required
def shortlist_applicant(applicant_id):
    if current_user.role != 'staff':
        flash('Access denied')
        return redirect(url_for('auth.login'))
    
    application = Application.query.get(applicant_id)
    if not application:
        flash('Application not found', 'danger')
        return redirect(url_for('staff.home'))
    
    success = App.controllers.shortlist_student(
        application.internship_id,
        application.student_id,
        current_user.id
    )
    
    if success:
        flash('Student shortlisted successfully!', 'success')
    else:
        flash('Failed to shortlist student')
    
    return redirect(url_for('staff.home', applicant_id=applicant_id))
