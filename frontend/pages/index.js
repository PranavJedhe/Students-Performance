import Link from "next/link";

export default function Home() {
  return (
    <div className="container">
      <h1>Student Performance</h1>

      <div style={{ marginBottom: "1rem" }}>
        <Link href="/admin">
          <button>Admin Module</button>
        </Link>{" "}
        <Link href="/student">
          <button>Student Module</button>
        </Link>{" "}
        <Link href="/rank-analytics">
          <button>Rank Analytics</button>
        </Link>{" "}
        <Link href="/report">
          <button>Report Module</button>
        </Link>
      </div>
    </div>
  );
}
