# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .auth import auth_views
from .admin import setup_admin
from flask import Blueprint, render_template, request, redirect, url_for
from App.models import Internship, db, Application, Student, Internship


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
    if not internship_id:
        return "Internship ID required", 400
    internship = Internship.query.get_or_404(internship_id)
    applications = Application.query.filter_by(internship_id=internship_id).all()
    shortlisted_students = [app.student for app in applications]
    selected_student = shortlisted_students[0] if shortlisted_students else None
    return render_template(
        'company_shortlist.html',
        internship=internship,
        shortlisted_students=shortlisted_students,
        selected_student=selected_student
    )

@login_landing_views.route('/staff/home', methods=['GET'])
def staff_home():
    return render_template('staff_home.html')

@login_landing_views.route('/student.html')
def student_html():
    return render_template('student.html')





views = [user_views, index_views, auth_views, login_landing_views]
# blueprints must be added to this list