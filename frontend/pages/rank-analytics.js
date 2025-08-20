import { useEffect, useState } from "react";

export default function RankAnalytics() {
  const [rankings, setRankings] = useState([]);

  useEffect(() => {
    fetch("/api/rank-analytics/rankings")
      .then((res) => res.json())
      .then((data) => setRankings(data.rankings || []));
  }, []);

  return (
    <div className="container">
      <h1>Rank Analytics Module</h1>
      <ul>
        {rankings.map((r) => (
          <li key={r.rank}>
            {r.rank}. {r.student} - GPA {r.gpa}
          </li>
        ))}
      </ul>
    </div>
  );
}
