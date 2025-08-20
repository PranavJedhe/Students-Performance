import '../styles/globals.css';
import Link from 'next/link';

export default function MyApp({ Component, pageProps }) {
  return (
    <>
      <nav className="top-nav">
        <Link href="/">Home</Link>
        <Link href="/admin">Admin</Link>
        <Link href="/student">Student</Link>
        <Link href="/rank-analytics">Rank Analytics</Link>
        <Link href="/report">Report</Link>
      </nav>
      <Component {...pageProps} />
    </>
  );
}
