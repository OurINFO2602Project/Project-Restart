# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .auth import auth_views
from .admin import setup_admin
from flask import Blueprint, render_template

login_landing_views = Blueprint('login_landing_views', __name__)

@login_landing_views.route('/login', methods=['GET'])
def login_landing():
    return render_template('login_landing.html')

@login_landing_views.route('/student/home', methods=['GET'])
def student_home():
    return render_template('student_base.html')

@login_landing_views.route('/company/home', methods=['GET'])
def company_home():
    # Mock data for demonstration
    internship = type('Internship', (object,), {'title': 'Software Intern', 'company': 'Acme Corp', 'id': 1})()
    shortlisted = [
        type('Student', (object,), {'name': 'Alice', 'degree': 'BSc Computer Science', 'gpa': 3.8, 'id': 1})(),
        type('Student', (object,), {'name': 'Bob', 'degree': 'BEng Software Engineering', 'gpa': 3.5, 'id': 2})()
    ]
    selected_student = shortlisted[0]
    return render_template('company1stpage.html', internship=internship, shortlisted=shortlisted, selected_student=selected_student)

@login_landing_views.route('/company/shortlist')
def company_shortlist():
    from flask import request
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

views = [user_views, index_views, auth_views, login_landing_views]
# blueprints must be added to this list