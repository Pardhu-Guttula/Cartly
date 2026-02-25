import { useState } from 'react';
import axios from 'axios';

const API_URL = "http://localhost:8000/api/promotions/apply";

const Home = () => {
  const [promoCode, setPromoCode] = useState("");
  const [promotion, setPromotion] = useState(null);
  const [error, setError] = useState("");

  const applyPromotion = async () => {
    try {
      const response = await axios.post(API_URL, { code: promoCode });
      setPromotion(response.data);
      setError("");
    } catch (err) {
      setError(err.response.data.detail);
      setPromotion(null);
    }
  };

  return (
    <div style={{ padding: "20px", maxWidth: "600px", margin: "auto" }}>
      <h1>Checkout Page</h1>
      <input
        type="text"
        value={promoCode}
        onChange={(e) => setPromoCode(e.target.value)}
        placeholder="Enter promotion code"
        style={{ width: "100%", padding: "10px", margin: "10px 0" }}
      />
      <button onClick={applyPromotion} style={{ padding: "10px", width: "100%" }}>
        Apply
      </button>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {promotion && (
        <div>
          <h2>Applied Promotion</h2>
          <p>Code: {promotion.code}</p>
          <p>Description: {promotion.description}</p>
          <p>Discount Amount: ${promotion.discount_amount}</p>
        </div>
      )}
    </div>
  );
};

export default Home;