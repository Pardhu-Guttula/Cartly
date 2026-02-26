import React from "react";
import { useIntl } from "react-intl";
import { Star } from "lucide-react";

export default function RatingStarsInteractive({ value = 0, size = 14, onStarClick = () => {} }) {
  const intl = useIntl();

  const full = Math.floor(value);
  const frac = Math.max(0, Math.min(1, value - full));

  return (
    <div className="flex items-center gap-[2px]">
      {Array.from({ length: 5 }).map((_, i) => {
        const fillPct = i < full ? 1 : i === full ? frac : 0;

        return (
          <button
            key={i}
            type="button"
            onClick={() => onStarClick(i + 1)}
            aria-label={intl.formatMessage(
              { id: "ratingStarsInteractive.rateStar" },
              { count: i + 1 }
            )}
            className="relative p-0 border-0 bg-transparent leading-none cursor-pointer"
            style={{ width: size, height: size }}
          >
            <Star size={size} color="#F59E0B" className="block" />
            <span
              aria-hidden="true"
              className="absolute inset-0 overflow-hidden"
              style={{ width: `${fillPct * 100}%` }}
            >
              <Star size={size} color="#F59E0B" fill="#F59E0B" className="block" />
            </span>
          </button>
        );
      })}
    </div>
  );
}