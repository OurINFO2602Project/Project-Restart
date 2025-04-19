from flask import Blueprint, redirect, render_template, request, jsonify, make_response, flash
from flask_jwt_extended import (
    jwt_required, 
    create_access_token, 
    get_jwt_identity,
    set_access_cookies,
    unset_jwt_cookies
)
from werkzeug.security import check_password_hash
from App.models import db, User, Company, Student, Internship, Shortlist
from datetime import timedelta

company_routes = Blueprint('company_routes', __name__, template_folder='../templates')

@company_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password) and user.type == 'company':
            access_token = create_access_token(identity=user.id, expires_delta=timedelta(days=1))
            resp = make_response(redirect(url_for('company_routes.company_dashboard')))
            set_access_cookies(resp, access_token)
            return resp
        
        flash("Invalid credentials")
    return render_template('401.html')

@company_routes.route('/logout')
def logout():
    resp = make_response(redirect(url_for('company_routes.login')))
    unset_jwt_cookies(resp)
    flash('Logged out successfully', 'info')
    return resp

@company_routes.route('/dashboard')
@jwt_required()
def company_dashboard():
    company_id = get_jwt_identity()
    company = Company.query.get(company_id)
    internships = company.internships
    return render_template('company/dashboard.html', internships=internships)

@company_routes.route('/shortlist/<int:internship_id>')
@jwt_required()
def view_shortlist(internship_id):
    company_id = get_jwt_identity()
    internship = Internship.query.filter_by(
        id=internship_id,
        company_id=company_id
    ).first_or_404()
    
    shortlisted = internship.shortlisted_students
    selected_id = request.args.get('selected')
    selected = next((s for s in shortlisted if s.id == int(selected_id)), None) if selected_id else None
    
    return render_template('company_shortlist.html',
                        internship=internship,
                        shortlisted=shortlisted,
                        selected_student=selected)

@company_routes.route('/student/<int:student_id>')
@jwt_required()
def view_student(student_id):
    student = Student.query.get(student_id)
    return jsonify({
        'name': student.name,
        'degree': student.degree,
        'gpa': student.gpa,
        'email': student.email,
        'graduation_year': student.graduation_year,
        'resume_url': student.resume_url
    })

@company_routes.route('/shortlist/add', methods=['POST'])
@jwt_required()
def add_to_shortlist():
    company_id = get_jwt_identity()
    data = request.get_json()
    
    internship = Internship.query.filter_by(
        id=data['internship_id'],
        company_id=company_id
    ).first()
    
    shortlist = Shortlist(
        internship_id=data['internship_id'],
        student_id=data['student_id']
    )
    db.session.add(shortlist)
    db.session.commit()
    
    return jsonify({'status': 'success'}), 201

@company_routes.route('/shortlist/remove/<int:shortlist_id>', methods=['DELETE'])
@jwt_required()
def remove_from_shortlist(shortlist_id):
    company_id = get_jwt_identity()
    shortlist = Shortlist.query.join(Internship).filter(
        Shortlist.id == shortlist_id,
        Internship.company_id == company_id
    ).first()
    
    db.session.delete(shortlist)
    db.session.commit()
    
    return jsonify({'status': 'deleted'}), 200

@company_routes.route('/internship/create', methods=['POST'])
@jwt_required()
def create_internship():
    company_id = get_jwt_identity()
    data = request.get_json()
    
    internship = Internship(
        title=data['title'],
        description=data['description'],
        company_id=company_id
    )
    db.session.add(internship)
    db.session.commit()
    
    return jsonify(internship.get_json()), 201
