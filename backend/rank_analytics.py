from flask import Blueprint, jsonify
from models import Student

# Sample data used by the report module when no database data is available
SAMPLE_RANKINGS = [
    {"rank": 1, "student": "Alice", "gpa": 4.0},
    {"rank": 2, "student": "Bob", "gpa": 3.9},
    {"rank": 3, "student": "Charlie", "gpa": 3.8},
]

rank_analytics_bp = Blueprint('rank_analytics', __name__)

@rank_analytics_bp.route('/api/rank-analytics')
def rank_root():
    """Root endpoint for the Rank Analytics module."""
    return jsonify(module='Rank Analytics module')


@rank_analytics_bp.route('/api/rank-analytics/rankings')
def rankings():
    """Return rankings computed from student GPA."""
    students = Student.query.order_by(Student.gpa.desc()).all()
    rankings = [
        {"rank": idx + 1, "student": s.name, "gpa": s.gpa}
        for idx, s in enumerate(students)
    ]
    return jsonify(rankings=rankings)
