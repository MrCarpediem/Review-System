import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [reviews, setReviews] = useState([]);
  const [search, setSearch] = useState("");
  const [error, setError] = useState(false);

  // Backend URL
  const API_URL = "http://127.0.0.1:8000/api/reviews";

  const loadReviews = async () => {
    try {
      setError(false);
      const res = await fetch(API_URL);
      if (!res.ok) throw new Error("Backend not responding");

      const data = await res.json();
      setReviews(data);
    } catch (err) {
      setError(true);
      console.log("Error:", err);
    }
  };

  useEffect(() => {
    loadReviews();
  }, []);

  const filtered = reviews.filter((r) =>
    r.product_name?.toLowerCase().includes(search.toLowerCase()) ||
    r.user_name?.toLowerCase().includes(search.toLowerCase()) ||
    r.contact_number?.includes(search)
  );

  return (
    <div className="container">
      <h1 className="title">📱 WhatsApp Product Review Dashboard</h1>

      {error && (
        <div className="error-box">❌ Backend Not Responding!</div>
      )}

      <input
        type="text"
        className="search"
        placeholder="Search reviews..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      <table className="reviews-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Contact</th>
            <th>User</th>
            <th>Product</th>
            <th>Review</th>
            <th>Created</th>
          </tr>
        </thead>

        <tbody>
          {!error && filtered.length === 0 ? (
            <tr>
              <td colSpan="6" className="no-data">No reviews found.</td>
            </tr>
          ) : (
            filtered.map((r) => (
              <tr key={r.id}>
                <td>{r.id}</td>
                <td>{r.contact_number}</td>
                <td>{r.user_name}</td>
                <td>{r.product_name}</td>
                <td>{r.product_review}</td>
                <td>{new Date(r.created_at).toLocaleString()}</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
}

export default App;
