from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from App.controllers.company import *
from App.models.internship import Internship
from App.models.shortlist import Shortlist
from App.models.student import Student

from App.controllers import(
    get_shortlisted_students,
    get_student_details,
    get_student_application_details
)

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
        return jsonify({"error": "Student not found"}), 404
        
    return jsonify(student)

@company_views.route('/api/students/<int:student_id>/details', methods=['GET'])
@jwt_required()
def get_student_application_details_api(student_id):
    if current_user.type != 'company':
        return jsonify({"error": "Unauthorized"}), 401

    student_details = get_student_details(student_id)
    if not student_details:
        return jsonify({"error": "Student not found"}), 404

    application_details = get_student_application_details(student_id)  # Fetch application-specific details
    if not application_details:
        return jsonify({"error": "Application details not found"}), 404

    return jsonify({
        "student": student_details,
        "application": application_details
    })
