import React, { useState } from "react";
import { ShoppingCart } from "lucide-react";
import { useIntl } from "react-intl";
import Section2RatingStars from "./Section2RatingStars";
import section2Styles from "./section2Styles";

export default function Section2ProductCard({
  imageUrl,
  category,
  title,
  rating,
  ratingCount,
  price,
  href = "http://localhost:8200/pdp.html",
  onProductClick = () => {},
  onAddToCart = () => {},
}) {
  const intl = useIntl();
  const [isHovered, setIsHovered] = useState(false);

  return (
    <div
      style={{
        ...section2Styles.card,
        boxShadow: isHovered ? section2Styles.cardShadowHover : section2Styles.cardShadow,
      }}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
    >
      <div style={section2Styles.imageWrap}>
        <img src={imageUrl} alt={title} style={section2Styles.image} />
      </div>

      <div style={section2Styles.body}>
        <div style={section2Styles.category}>{String(category).toUpperCase()}</div>

        <a
          href={href}
          onClick={(e) => {
            onProductClick(e);
          }}
          style={section2Styles.titleLink}
        >
          <div style={section2Styles.titleClamp}>{title}</div>
        </a>

        <div style={section2Styles.ratingRow}>
          <Section2RatingStars value={rating} styles={section2Styles} />
          <div style={section2Styles.ratingCount}>({ratingCount})</div>
        </div>

        <div style={section2Styles.priceRow}>
          <div style={section2Styles.price}>{price}</div>
        </div>

        <button
          type="button"
          onClick={onAddToCart}
          style={{
            ...section2Styles.addBtn,
            backgroundColor: isHovered ? "#3B5BFF" : "#4361EE",
          }}
        >
          <ShoppingCart size={14} color="#FFFFFF" />
          <span style={section2Styles.addBtnLabel}>
            {intl.formatMessage({ id: "common.addToCart" })}
          </span>
        </button>
      </div>
    </div>
  );
}