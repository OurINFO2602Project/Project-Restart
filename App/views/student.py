from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_jwt_extended import current_user, jwt_required
from App.controllers.application import create_application
from App.models import Internship
from App import db

# Create a blueprint for the student application
student_views = Blueprint('student_views', __name__, template_folder='../templates')

@student_views.route('/apply/<int:internship_id>', methods=['GET', 'POST'])
@jwt_required()
def apply_to_internship(internship_id):
    internship = Internship.query.get(internship_id)
    if request.method == 'POST':
        degree = request.form['degree']
        gpa = float(request.form['gpa'])
        graduation_year = int(request.form['graduation_year'])
        resume_url = request.form['resume_url']

        application = create_application(
            internship_id=internship_id,
            student_id=current_user.id,
            degree=degree,
            gpa=gpa,
            graduation_year=graduation_year,
            resume_url=resume_url
        )
        
        flash('Application submitted!')
        return redirect(url_for('student_views.apply_to_internship', internship_id=internship_id))
    
    elif request.method == 'GET':
        return render_template('student.html', internships=Internship.query.all(), current_user=current_user, selected_internship=internship)

