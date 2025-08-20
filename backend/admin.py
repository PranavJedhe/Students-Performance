from flask import Blueprint, jsonify, request
from models import db, Department, Course, Student

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/api/admin')
def admin_root():
    """Root endpoint for the Admin module."""
    return jsonify(module='Admin module')

# Department endpoints
@admin_bp.route('/api/admin/departments', methods=['GET', 'POST'])
def departments():
    if request.method == 'POST':
        data = request.get_json() or {}
        name = data.get('name')
        if not name:
            return jsonify(error='Name required'), 400
        dept = Department(name=name)
        db.session.add(dept)
        db.session.commit()
        return jsonify(id=dept.id, name=dept.name), 201
    depts = Department.query.all()
    return jsonify(departments=[{'id': d.id, 'name': d.name} for d in depts])

@admin_bp.route('/api/admin/departments/<int:dept_id>', methods=['DELETE'])
def delete_department(dept_id):
    dept = Department.query.get_or_404(dept_id)
    db.session.delete(dept)
    db.session.commit()
    return jsonify(success=True)

# Course endpoints
@admin_bp.route('/api/admin/courses', methods=['GET', 'POST'])
def courses():
    if request.method == 'POST':
        data = request.get_json() or {}
        name = data.get('name')
        department_id = data.get('department_id')
        if not name or not department_id:
            return jsonify(error='Name and department_id required'), 400
        course = Course(name=name, department_id=department_id)
        db.session.add(course)
        db.session.commit()
        return jsonify(id=course.id, name=course.name, department_id=course.department_id), 201
    courses = Course.query.all()
    return jsonify(courses=[{'id': c.id, 'name': c.name, 'department_id': c.department_id} for c in courses])

@admin_bp.route('/api/admin/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    return jsonify(success=True)

# Student endpoints
@admin_bp.route('/api/admin/students', methods=['GET', 'POST'])
def students():
    if request.method == 'POST':
        data = request.get_json() or {}
        name = data.get('name')
        course_id = data.get('course_id')
        gpa = data.get('gpa', 0)
        if not name or not course_id:
            return jsonify(error='Name and course_id required'), 400
        student = Student(name=name, course_id=course_id, gpa=gpa)
        db.session.add(student)
        db.session.commit()
        return jsonify(id=student.id, name=student.name, course_id=student.course_id, gpa=student.gpa), 201
    students = Student.query.all()
    return jsonify(students=[{'id': s.id, 'name': s.name, 'course_id': s.course_id, 'gpa': s.gpa} for s in students])

@admin_bp.route('/api/admin/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return jsonify(success=True)
