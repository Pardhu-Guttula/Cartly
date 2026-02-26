import React, { useState } from "react";
import RatingStars from "./RatingStars";
import AddToCartButton from "./AddToCartButton";

export default function ProductCardSection2({
  imageUrl,
  category,
  title,
  rating,
  ratingCount,
  price,
  onAddToCart = () => {},
  onProductClick = () => {},
}) {
  const [isHovered, setIsHovered] = useState(false);

  return (
    <div
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      style={{
        background: "#FFFFFF",
        borderRadius: 16,
        overflow: "hidden",
        boxShadow: "0px 1px 3px 0px rgba(0,0,0,0.1), 0px 1px 2px 0px rgba(0,0,0,0.06)",
        display: "flex",
        flexDirection: "column",
        minHeight: 520,
      }}
    >
      <div
        style={{
          height: 280,
          background: "#F8FAFC",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          padding: 24,
        }}
      >
        <img
          src={imageUrl}
          alt={title}
          style={{
            maxHeight: 224,
            maxWidth: 264.53,
            width: "auto",
            height: "auto",
            objectFit: "contain",
            filter: isHovered ? "saturate(1.02)" : "none",
            transition: "filter 150ms ease",
          }}
        />
      </div>

      <div
        style={{
          paddingLeft: 20,
          paddingRight: 20,
          paddingTop: 24.25,
          paddingBottom: 20,
          display: "flex",
          flexDirection: "column",
          gap: 1.4,
          flex: 1,
        }}
      >
        <div
          style={{
            fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif",
            fontSize: 12,
            fontWeight: 600,
            letterSpacing: 0.5,
            textTransform: "uppercase",
            color: "#4361EE",
            lineHeight: "19.2px",
          }}
        >
          {category}
        </div>

        <button
          type="button"
          onClick={onProductClick}
          style={{
            border: 0,
            background: "transparent",
            padding: 0,
            textAlign: "left",
            cursor: "pointer",
            color: "#1E293B",
            fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif",
            fontSize: 15,
            fontWeight: 600,
            lineHeight: "21px",
            minHeight: 42,
            display: "-webkit-box",
            WebkitLineClamp: 2,
            WebkitBoxOrient: "vertical",
            overflow: "hidden",
          }}
          title={title}
        >
          {title}
        </button>

        <div style={{ display: "flex", alignItems: "center", gap: 8, paddingTop: 8.6 }}>
          <RatingStars value={rating} />
          <div
            style={{
              fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif",
              fontSize: 13,
              fontWeight: 400,
              color: "#64748B",
              lineHeight: "20.8px",
            }}
          >
            ({ratingCount})
          </div>
        </div>

        <div style={{ paddingTop: 10.59, paddingBottom: 14.6 }}>
          <div
            style={{
              fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif",
              fontSize: 20,
              fontWeight: 700,
              color: "#4361EE",
              lineHeight: "32px",
            }}
          >
            {price}
          </div>
        </div>

        <div style={{ marginTop: "auto" }}>
          <AddToCartButton onClick={onAddToCart} />
        </div>
      </div>
    </div>
  );
}