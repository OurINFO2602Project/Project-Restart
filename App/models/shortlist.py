class Shortlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    internship_id = db.Column(db.Integer, db.ForeignKey('internship.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    student = db.relationship('Student', backref=db.backref('shortlists', lazy=True))
    internship = db.relationship('Internship', backref=db.backref('shortlisted_students', lazy=True))
    
    def get_json(self):
        return {
            "id": self.id,
            "internship_id": self.internship_id,
            "internship": self.internship.title,
            "student_id": self.student_id,
            "student": self.student.username,
        }
