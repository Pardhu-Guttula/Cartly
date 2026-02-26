import React from "react";
import { Star } from "lucide-react";

export default function Section2RatingStars({ value, max = 5, styles = {} }) {
  const filled = Math.max(0, Math.min(max, Math.floor(value)));
  return (
    <div style={styles.starsRow} aria-label={`Rating ${value} out of ${max}`}>
      {Array.from({ length: max }).map((_, i) => {
        const isFilled = i < filled;
        return (
          <Star
            key={i}
            size={13}
            style={{
              ...styles.starIcon,
              fill: isFilled ? "#F59E0B" : "transparent",
              color: "#F59E0B",
              opacity: isFilled ? 1 : 0.55,
            }}
          />
        );
      })}
    </div>
  );
}