import os
from flask import Flask, jsonify
from models import db, Department, Course

from admin import admin_bp
from student import student_bp
from rank_analytics import rank_analytics_bp
from report import report_bp

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = os.environ.get("DATABASE_URL", "sqlite:///college.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Pre-populate department and course data if the tables are empty
def seed_data():
    department_names = [
        "Mathematics",
        "Physics",
        "Chemistry",
        "Biology",
        "Computer Science",
        "Environmental Science",
        "Biotechnology",
        "Microbiology",
        "Zoology",
        "Botany",
        "Statistics",
        "Geology",
        "Biochemistry",
    ]

    course_names = [
        "Mathematics",
        "Physics",
        "Chemistry",
        "Biology",
        "Computer Science",
        "Biotechnology",
        "Zoology",
        "Botany",
        "Statistics",
    ]

    if Department.query.count() == 0:
        for name in department_names:
            db.session.add(Department(name=name))
        db.session.commit()

    if Course.query.count() == 0:
        for name in course_names:
            dept = Department.query.filter_by(name=name).first()
            if dept:
                db.session.add(Course(name=name, department_id=dept.id))
        db.session.commit()

# Create database tables before the first request. Flask 3 removed
# the `before_first_request` decorator, so we initialize the tables
# when the application starts instead.
with app.app_context():
    db.create_all()
    seed_data()

app.register_blueprint(admin_bp)
app.register_blueprint(student_bp)
app.register_blueprint(rank_analytics_bp)
app.register_blueprint(report_bp)

@app.route('/api/hello')
def hello():
    return jsonify(message='Hello from Flask backend!')

if __name__ == '__main__':
    app.run(debug=True, port=5002)
