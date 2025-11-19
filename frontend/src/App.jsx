import { useEffect, useState } from "react";
import axios from "axios";

export default function App() {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/api/reviews").then(res => {
      setReviews(res.data);
    });
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Saved Reviews</h1>
      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>Name</th>
            <th>Product</th>
            <th>Rating</th>
            <th>Review</th>
          </tr>
        </thead>
        <tbody>
          {reviews.map(r => (
            <tr key={r.id}>
              <td>{r.user_name}</td>
              <td>{r.product_name}</td>
              <td>{r.rating}</td>
              <td>{r.product_review}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
