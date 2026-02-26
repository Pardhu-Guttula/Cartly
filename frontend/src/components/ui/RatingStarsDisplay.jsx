import React, { useMemo } from "react";
import { useIntl } from "react-intl";
import { Star } from "lucide-react";

export default function RatingStarsDisplay({ value = 0, size = 14 }) {
  const intl = useIntl();

  const stars = useMemo(() => {
    const v = Math.max(0, Math.min(5, Number(value) || 0));
    const full = Math.floor(v);
    const frac = v - full;
    const hasHalf = frac >= 0.25 && frac < 0.75;
    const extraFull = frac >= 0.75 ? 1 : 0;
    const filled = Math.min(5, full + extraFull);
    const halfIndex = hasHalf ? filled : -1;
    return { filled, halfIndex };
  }, [value]);

  return (
    <span
      className="inline-flex items-center gap-[2px]"
      aria-label={intl.formatMessage({ id: "ratingStarsDisplay.ariaLabel" }, { value })}
    >
      {Array.from({ length: 5 }).map((_, i) => {
        const isFull = i < stars.filled;
        const isHalf = i === stars.halfIndex;

        if (isHalf) {
          return (
            <span
              key={i}
              className="relative inline-block"
              style={{ width: size, height: size }}
              aria-hidden="true"
            >
              <Star
                size={size}
                className="absolute inset-0"
                style={{
                  color: "#F59E0B",
                  fill: "transparent",
                }}
              />
              <span className="absolute inset-0 overflow-hidden" style={{ width: "50%" }}>
                <Star size={size} style={{ color: "#F59E0B", fill: "#F59E0B" }} />
              </span>
            </span>
          );
        }

        return (
          <Star
            key={i}
            size={size}
            aria-hidden="true"
            style={{
              color: "#F59E0B",
              fill: isFull ? "#F59E0B" : "transparent",
            }}
          />
        );
      })}
    </span>
  );
}