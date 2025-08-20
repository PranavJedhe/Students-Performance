from flask import Blueprint, jsonify, request

# Very naive authentication example
USERS = {"alice": "password"}

PERFORMANCE = {
    "alice": {"gpa": 3.8, "completed_courses": ["Algorithms"]}
}

student_bp = Blueprint('student', __name__)

@student_bp.route('/api/student')
def student_root():
    """Root endpoint for the Student module."""
    return jsonify(module='Student module')


@student_bp.route('/api/student/login', methods=['POST'])
def login():
    """Very basic login check."""
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    if USERS.get(username) == password:
        return jsonify(success=True)
    return jsonify(success=False), 401


@student_bp.route('/api/student/performance')
def performance():
    """Return fake performance data for a hard-coded user."""
    return jsonify(PERFORMANCE.get('alice', {}))
