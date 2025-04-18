from flask import Blueprint, render_template, request, redirect, url_for, flash
from App.models import Student, Application
from App import db

# Create a blueprint for the student application
app = Blueprint('student', __name__)


@app.route('/apply', methods=['GET', 'POST'])
def apply():
    if request.method == 'POST':
        student_id = request.form['student_id']
        degree = request.form['degree']
        graduation_year = request.form['graduation_year']
        gpa = request.form['gpa']

        db.session.add(Student(student_id=student_id, degree=degree, graduation_year=graduation_year, gpa=gpa))
        db.session.commit()
        flash('Application submitted successfully!', 'success')
    return render_template('student_home.html')
    