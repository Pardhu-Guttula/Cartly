# Epic Title: Develop Frontend Interface for Promotions

import { useState } from 'react';

export default function Home() {
  const [promotionCode, setPromotionCode] = useState('');
  const [message, setMessage] = useState('');
  const [totalPrice, setTotalPrice] = useState(100);
  const [discountedPrice, setDiscountedPrice] = useState(100);
  const [appliedPromotion, setAppliedPromotion] = useState(null);

  const applyPromotion = async () => {
    try {
      const response = await fetch('/api/apply_promotion', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ promotion_code: promotionCode, order_total: totalPrice }),
      });

      const result = await response.json();
      if (response.ok) {
        setAppliedPromotion(result);
        setDiscountedPrice(result.discounted_amount);
      } else {
        setMessage(result.error);
      }
    } catch (error) {
      setMessage('An error occurred while applying the promotion.');
    }
  };

  return (
    <div className="container">
      <h1>Checkout Page</h1>
      <div>
        <input
          type="text"
          placeholder="Enter promotion code"
          value={promotionCode}
          onChange={(e) => setPromotionCode(e.target.value)}
        />
        <button onClick={applyPromotion}>Apply</button>
      </div>
      {message && <p>{message}</p>}
      {appliedPromotion && (
        <div>
          <h2>Applied Promotion</h2>
          <p>Code: {appliedPromotion.promotion_code}</p>
          <p>Discount Amount: ${totalPrice - discountedPrice}</p>
        </div>
      )}
      <h2>Total Price: ${discountedPrice}</h2>
    </div>
  );
}