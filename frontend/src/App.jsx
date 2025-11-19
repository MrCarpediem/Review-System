import { useEffect, useState } from "react";

function App() {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/reviews")
      .then((res) => res.json())
      .then((data) => setReviews(data));
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>Reviews</h1>
      {!reviews.length && <p>No reviews yet.</p>}

      {reviews.map((r) => (
        <div key={r.id} style={{ border: "1px solid #ccc", padding: 10, marginBottom: 10 }}>
          <p><b>Phone:</b> {r.phone}</p>
          <p><b>Product:</b> {r.product}</p>
          <p><b>Rating:</b> {r.rating}</p>
          <p><b>Comment:</b> {r.comment}</p>
        </div>
      ))}
    </div>
  );
}

export default App;
