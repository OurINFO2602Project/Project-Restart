# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .auth import auth_views
from .admin import setup_admin
from flask import Blueprint, render_template, request, redirect, url_for
from App.models import Internship, db

login_landing_views = Blueprint('login_landing_views', __name__)

internships = []

@login_landing_views.route('/login', methods=['GET'])
def login_landing():
    return render_template('login_landing.html')

@login_landing_views.route('/student/home', methods=['GET'])
def student_home():
    return render_template('student_base.html')

@login_landing_views.route('/company/home', methods=['GET', 'POST'])
def company_home():
    if request.method == 'POST':
        title = request.form['title']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        salary = request.form['salary']
        description = request.form['description']
        new_internship = Internship(
            title=title,
            start_date=start_date,
            end_date=end_date,
            salary=salary,
            description=description
        )
        new_internship.company_id = 1  # Set company_id after creation
        db.session.add(new_internship)
        db.session.commit()
        return redirect(url_for('login_landing_views.company_home'))
    internships = Internship.query.all()
    return render_template('company1stpage.html', internships=internships)

@login_landing_views.route('/company/shortlist')
def company_shortlist():
    internship_id = request.args.get('internship_id')
    selected = request.args.get('selected')
    internship = type('Internship', (object,), {'title': 'Software Intern', 'company': 'Acme Corp', 'id': internship_id})()
    # Mock students
    students = {
        '1': type('Student', (object,), {
            'name': 'Alice', 'degree': 'BSc Computer Science', 'gpa': 3.8, 'id': 1,
            'email': 'alice@example.com', 'resume_url': '#'
        })(),
        '2': type('Student', (object,), {
            'name': 'Bob', 'degree': 'BEng Software Engineering', 'gpa': 3.5, 'id': 2,
            'email': 'bob@example.com', 'resume_url': '#'
        })()
    }
    selected_student = students.get(selected)
    return render_template('company_shortlist.html', internship=internship, selected_student=selected_student)

@login_landing_views.route('/staff/home', methods=['GET'])
def staff_home():
    return render_template('staff_home.html')

@login_landing_views.route('/student.html')
def student_html():
    return render_template('student.html')

views = [user_views, index_views, auth_views, login_landing_views]
# blueprints must be added to this list