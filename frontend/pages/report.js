import { useState } from "react";

export default function Report() {
  const [message, setMessage] = useState(null);

  const exportReport = () => {
    setMessage("Generating PDF...");
    window.open("/api/report/export", "_blank");
  };

  return (
    <div className="container">
      <h1>Report Module</h1>
      <button onClick={exportReport}>Export Report</button>
      {message && <p>{message}</p>}
    </div>
  );
}
