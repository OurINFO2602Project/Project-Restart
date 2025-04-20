from flask import Blueprint, render_template, jsonify
from flask_jwt_extended import jwt_required, current_user

from App.controllers import(
    get_shortlisted_students,
    get_student_details,
    get_student_application_details
)

company_views = Blueprint('company_views', __name__, template_folder='../templates')

@company_views.route('/company/internships/<int:internship_id>/shortlist', methods=['GET'])
@jwt_required()
def view_shortlist(internship_id):
    if current_user.type != 'company':
        return render_template('401.html', error="Only companies can view shortlists"), 401
        
    shortlisted_students = get_shortlisted_students(internship_id)
    selected_student = None if not shortlisted_students else shortlisted_students[0]
    
    return render_template('company_shortlist.html',
                         shortlisted_students=shortlisted_students,
                         selected_student=selected_student)

@company_views.route('/api/students/<int:student_id>', methods=['GET'])
@jwt_required()
def get_student_details_api(student_id):
    if current_user.type != 'company':
        return jsonify({"error": "Unauthorized"}), 401
        
    student = get_student_details(student_id)
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