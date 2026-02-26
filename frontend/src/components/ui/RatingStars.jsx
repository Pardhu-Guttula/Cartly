import React from "react";
import { Star } from "lucide-react";

export default function RatingStars({ value, max = 5 }) {
  const filled = Math.floor(value);
  const hasHalf = value - filled >= 0.5;

  return (
    <div style={{ display: "flex", alignItems: "center", gap: 2 }}>
      {Array.from({ length: max }).map((_, i) => {
        const isFilled = i < filled;
        const isHalf = !isFilled && hasHalf && i === filled;

        return (
          <span
            key={i}
            aria-hidden="true"
            style={{
              width: 14,
              height: 14,
              display: "inline-flex",
              color: "#F59E0B",
              opacity: isFilled || isHalf ? 1 : 0.35,
            }}
          >
            <Star
              size={14}
              strokeWidth={1.5}
              fill={isFilled || isHalf ? "currentColor" : "none"}
            />
          </span>
        );
      })}
    </div>
  );
}