import { useState } from "react";

export default function Student() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loggedIn, setLoggedIn] = useState(false);
  const [performance, setPerformance] = useState(null);

  const handleLogin = async (e) => {
    e.preventDefault();
    const res = await fetch("/api/student/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password }),
    });
    if (res.ok) {
      setLoggedIn(true);
    }
  };

  const loadPerformance = async () => {
    const res = await fetch("/api/student/performance");
    const data = await res.json();
    setPerformance(data);
  };

  return (
    <div className="container">
      <h1>Student Module</h1>
      {!loggedIn ? (
        <form onSubmit={handleLogin}>
          <div>
            <label>
              Username:
              <input
                value={username}
                onChange={(e) => setUsername(e.target.value)}
              />
            </label>
          </div>
          <div>
            <label>
              Password:
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </label>
          </div>
          <button type="submit">Login</button>
        </form>
      ) : (
        <div>
          <button onClick={loadPerformance}>Load Performance</button>
          {performance && (
            <div>
              <p>GPA: {performance.gpa}</p>
              <p>
                Completed Courses:
                {performance.completed_courses.join(", ")}
              </p>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
