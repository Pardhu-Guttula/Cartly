import React, { useState } from "react";
import { useIntl } from "react-intl";
import { Heart, ShoppingCart } from "lucide-react";
import RatingStarsInteractive from "./RatingStarsInteractive";
import clampStyles from "../utils/clampStyles";
import formatPrice from "../utils/formatPrice";

export default function ProductCard({
  id,
  imageSrc,
  imageAlt,
  category,
  title,
  ratingValue,
  reviewCount,
  price,
  href = "http://localhost:8200/pdp.html",
  onNavigate = () => {},
  onAddToCart = () => {},
  onToggleWishlist = () => {},
}) {
  const intl = useIntl();

  const [isHovered, setIsHovered] = useState(false);
  const [wishlisted, setWishlisted] = useState(false);

  return (
    <article
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      className="bg-white rounded-xl shadow-sm overflow-hidden flex flex-col min-h-[360px]"
    >
      <div className="bg-slate-50 h-[160px] p-4 flex items-center justify-center relative">
        <img
          src={imageSrc}
          alt={imageAlt || title}
          className="max-w-[200px] max-h-[132px] w-auto h-auto object-contain block"
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
            aria-label={
              wishlisted
                ? intl.formatMessage({ id: "productCard.removeFromWishlist" })
                : intl.formatMessage({ id: "productCard.addToWishlist" })
            }
            onClick={() => {
              const next = !wishlisted;
              setWishlisted(next);
              onToggleWishlist(id, next);
            }}
            className="w-9 h-9 rounded-full border-0 bg-white shadow-md grid place-items-center cursor-pointer"
          >
            <Heart size={18} color="#334155" fill={wishlisted ? "#334155" : "transparent"} />
          </button>
        </div>
      </div>

      <div className="px-4 pt-3 pb-3 flex flex-col gap-2 flex-1">
        <div className="text-[#4361EE] text-[9px] font-semibold tracking-[0.6px] uppercase leading-4 font-sans">
          {category}
        </div>

        <a
          href={href}
          onClick={(e) => {
            e.preventDefault();
            onNavigate(id);
          }}
          className="text-slate-800 text-[12px] font-semibold leading-[16px] no-underline min-h-[32px] font-sans"
          style={clampStyles(2)}
        >
          {title}
        </a>

        <div className="flex items-center gap-2 pt-0.5">
          <RatingStarsInteractive value={ratingValue} onStarClick={() => {}} size={12} />
          <div className="text-slate-500 text-[11px] leading-4 font-sans">({reviewCount})</div>
        </div>

        <div className="pt-0.5 pb-1.5">
          <div className="text-[#4361EE] text-[14px] font-bold leading-5 font-sans">
            {formatPrice(price)}
          </div>
        </div>

        <button
          type="button"
          onClick={() => onAddToCart(id)}
          className="mt-auto w-full rounded-lg bg-[#4361EE] text-white py-2 flex items-center justify-center gap-2 cursor-pointer text-[12px] font-semibold font-sans"
        >
          <ShoppingCart size={14} color="#FFFFFF" />
          {intl.formatMessage({ id: "common.addToCart" })}
        </button>
      </div>
    </article>
  );
}