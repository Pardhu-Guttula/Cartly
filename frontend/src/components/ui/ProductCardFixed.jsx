import React, { useState } from "react";
import { useIntl } from "react-intl";
import { Heart, ShoppingCart } from "lucide-react";
import RatingStarsDisplay from "./RatingStarsDisplay";
import clampStyles from "../utils/clampStyles";

export default function ProductCardFixed({
  id,
  imageSrc,
  imageAlt,
  category,
  title,
  href,
  ratingValue,
  reviewCount,
  price,
  onNavigate = () => {},
  onAddToCart = () => {},
  onToggleWishlist = () => {},
}) {
  const intl = useIntl();

  const [isHovered, setIsHovered] = useState(false);
  const [wishlisted, setWishlisted] = useState(false);

  const handleWishlist = () => {
    const next = !wishlisted;
    setWishlisted(next);
    onToggleWishlist(id, next);
  };

  return (
    <article
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      className="w-[331px] min-h-[360px] bg-white rounded-xl overflow-hidden shadow-sm flex flex-col"
    >
      <div className="h-[160px] bg-slate-50 p-4 flex items-center justify-center relative">
        <img
          src={imageSrc}
          alt={imageAlt || title}
          className="max-w-[200px] max-h-[132px] w-auto h-auto object-contain"
          loading="lazy"
        />

        <div
          className={[
            "absolute top-3 right-2 transition-all duration-150",
            isHovered
              ? "opacity-100 translate-y-0 pointer-events-auto"
              : "opacity-0 -translate-y-0.5 pointer-events-none",
          ].join(" ")}
        >
          <button
            type="button"
            onClick={handleWishlist}
            aria-label={
              wishlisted
                ? intl.formatMessage({ id: "productCardFixed.removeFromWishlist" })
                : intl.formatMessage({ id: "productCardFixed.addToWishlist" })
            }
            className="w-9 h-9 rounded-full border border-slate-900/10 bg-white shadow-md inline-flex items-center justify-center cursor-pointer"
          >
            <Heart
              size={18}
              style={{
                color: wishlisted ? "#4361EE" : "#334155",
                fill: wishlisted ? "#4361EE" : "transparent",
              }}
            />
          </button>
        </div>
      </div>

      <div className="px-4 pt-3 pb-3 flex flex-col gap-2 flex-1">
        <div className="font-sans text-[9px] font-semibold tracking-[0.6px] uppercase text-[#4361EE] leading-4 whitespace-nowrap">
          {category}
        </div>

        <a
          href={href}
          onClick={(e) => {
            e.preventDefault();
            onNavigate(id, href);
          }}
          className="no-underline text-slate-800 font-sans text-[12px] font-semibold leading-[16px] min-h-[32px]"
          style={clampStyles(2)}
        >
          {title}
        </a>

        <div className="flex items-center gap-2 pt-0.5">
          <RatingStarsDisplay value={ratingValue} size={12} />
          <span className="font-sans text-[11px] font-normal leading-4 text-slate-500 whitespace-nowrap">
            ({reviewCount})
          </span>
        </div>

        <div className="pt-0.5 pb-1.5">
          <div className="font-sans text-[14px] font-bold leading-5 text-[#4361EE]">{price}</div>
        </div>

        <button
          type="button"
          onClick={() => onAddToCart(id)}
          className="mt-auto w-full h-9 rounded-lg border border-[#4361EE]/35 bg-[#4361EE] text-white inline-flex items-center justify-center gap-2 font-sans text-[12px] font-semibold cursor-pointer"
        >
          <ShoppingCart size={14} className="text-white" />
          <span>{intl.formatMessage({ id: "common.addToCart" })}</span>
        </button>
      </div>
    </article>
  );
}