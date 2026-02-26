import React, { useState } from "react";
import { Heart, ShoppingCart } from "lucide-react";
import { useIntl } from "react-intl";
import RatingStars from "./RatingStars";
import PrimaryButton from "./PrimaryButton";
import styles from "./styles";

export default function ProductCard({
  imageUrl,
  category,
  title,
  rating,
  ratingCount,
  price,
  href = "http://localhost:8200/pdp.html",
  onAddToCart = () => {},
  onToggleWishlist = () => {},
  isWishlisted = false,
  onNavigate = () => {},
}) {
  const intl = useIntl();
  const [isHovered, setIsHovered] = useState(false);

  return (
    <article
      style={styles.card}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
    >
      <div style={styles.imageArea}>
        <img src={imageUrl} alt={title} style={styles.productImage} loading="lazy" />

        <div
          style={{
            ...styles.actionsOverlay,
            opacity: isHovered ? 1 : 0,
            pointerEvents: isHovered ? "auto" : "none",
            transform: isHovered ? "translateY(0px)" : "translateY(-2px)",
          }}
        >
          <button
            type="button"
            onClick={onToggleWishlist}
            aria-pressed={isWishlisted}
            aria-label={
              isWishlisted
                ? intl.formatMessage({ id: "productCard.wishlist.remove" })
                : intl.formatMessage({ id: "productCard.wishlist.add" })
            }
            style={styles.wishlistButton}
          >
            <Heart
              size={16}
              style={{
                color: "#334155",
                fill: isWishlisted ? "#334155" : "transparent",
              }}
            />
          </button>
        </div>
      </div>

      <div style={styles.body}>
        <div style={styles.category}>{category}</div>

        <h3 style={styles.title}>
          <a
            href={href}
            onClick={(e) => {
              e.preventDefault();
              onNavigate(href);
            }}
            style={styles.titleLink}
            title={title}
          >
            {title}
          </a>
        </h3>

        <div style={styles.ratingRow}>
          <RatingStars value={rating} styles={styles} />
          <span style={styles.ratingCount}>({ratingCount})</span>
        </div>

        <div style={styles.priceRow}>
          <span style={styles.price}>{price}</span>
        </div>

        <div style={styles.ctaRow}>
          <PrimaryButton
            label={intl.formatMessage({ id: "common.addToCart" })}
            onClick={onAddToCart}
            iconLeft={<ShoppingCart size={14} color="#FFFFFF" />}
            styles={styles}
          />
        </div>
      </div>
    </article>
  );
}