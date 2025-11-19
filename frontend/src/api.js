import { BASE_URL } from "./config";

export async function fetchReviews() {
  try {
    const res = await fetch(`${BASE_URL}/api/reviews`);
    return await res.json();
  } catch (err) {
    console.error("Fetch Error:", err);
    return null;
  }
}

export async function deleteReview(id) {
  try {
    const res = await fetch(`${BASE_URL}/api/review/${id}`, {
      method: "DELETE"
    });
    return await res.json();
  } catch (err) {
    console.error("Delete Error:", err);
    return null;
  }
}
