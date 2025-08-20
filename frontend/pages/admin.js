import { useEffect, useState } from "react";

export default function Admin() {
  const [departments, setDepartments] = useState([]);
  const [courses, setCourses] = useState([]);
  const [students, setStudents] = useState([]);
  const [deptName, setDeptName] = useState("");
  const [courseName, setCourseName] = useState("");
  const [courseDept, setCourseDept] = useState("");
  const [studentName, setStudentName] = useState("");
  const [studentCourse, setStudentCourse] = useState("");
  const [studentGpa, setStudentGpa] = useState("");

  const loadData = () => {
    fetch("/api/admin/departments")
      .then((res) => res.json())
      .then((data) => setDepartments(data.departments || []));
    fetch("/api/admin/courses")
      .then((res) => res.json())
      .then((data) => setCourses(data.courses || []));
    fetch("/api/admin/students")
      .then((res) => res.json())
      .then((data) => setStudents(data.students || []));
  };

  useEffect(() => {
    loadData();
  }, []);

  const addDepartment = async () => {
    await fetch("/api/admin/departments", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name: deptName }),
    });
    setDeptName("");
    loadData();
  };

  const addCourse = async () => {
    await fetch("/api/admin/courses", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name: courseName, department_id: courseDept }),
    });
    setCourseName("");
    setCourseDept("");
    loadData();
  };

  const addStudent = async () => {
    await fetch("/api/admin/students", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name: studentName,
        course_id: studentCourse,
        gpa: parseFloat(studentGpa) || 0,
      }),
    });
    setStudentName("");
    setStudentCourse("");
    setStudentGpa("");
    loadData();
  };

  const deleteDepartment = async (id) => {
    await fetch(`/api/admin/departments/${id}`, { method: "DELETE" });
    loadData();
  };

  const deleteCourse = async (id) => {
    await fetch(`/api/admin/courses/${id}`, { method: "DELETE" });
    loadData();
  };

  const deleteStudent = async (id) => {
    await fetch(`/api/admin/students/${id}`, { method: "DELETE" });
    loadData();
  };

  return (
    <div className="container">
      <h1>Admin Module</h1>
      <h2>Departments</h2>
      <input
        value={deptName}
        onChange={(e) => setDeptName(e.target.value)}
        placeholder="New department"
      />
      <button onClick={addDepartment}>Add</button>
      <ul>
        {departments.map((d) => (
          <li key={d.id}>
            {d.name} <button onClick={() => deleteDepartment(d.id)}>Delete</button>
          </li>
        ))}
      </ul>

      <h2>Courses</h2>
      <input
        value={courseName}
        onChange={(e) => setCourseName(e.target.value)}
        placeholder="New course"
      />
      <input
        value={courseDept}
        onChange={(e) => setCourseDept(e.target.value)}
        placeholder="Department id"
        style={{ width: "120px" }}
      />
      <button onClick={addCourse}>Add</button>
      <ul>
        {courses.map((c) => (
          <li key={c.id}>
            {c.name} (dept {c.department_id})
            <button onClick={() => deleteCourse(c.id)}>Delete</button>
          </li>
        ))}
      </ul>

      <h2>Students</h2>
      <input
        value={studentName}
        onChange={(e) => setStudentName(e.target.value)}
        placeholder="New student"
      />
      <input
        value={studentCourse}
        onChange={(e) => setStudentCourse(e.target.value)}
        placeholder="Course id"
        style={{ width: "120px" }}
      />
      <input
        value={studentGpa}
        onChange={(e) => setStudentGpa(e.target.value)}
        placeholder="GPA"
        style={{ width: "80px" }}
      />
      <button onClick={addStudent}>Add</button>
      <ul>
        {students.map((s) => (
          <li key={s.id}>
            {s.name} (GPA {s.gpa})
            <button onClick={() => deleteStudent(s.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
