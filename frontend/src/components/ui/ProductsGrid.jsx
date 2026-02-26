import React, { useMemo } from "react";
import ProductCard from "./ProductCard";
import styles from "./styles";

export default function ProductsGrid({
  products,
  onAddToCart = () => {},
  onToggleWishlist = () => {},
  wishlistedIds = [],
  onNavigate = () => {},
}) {
  const wishlistedSet = useMemo(() => new Set(wishlistedIds), [wishlistedIds]);

  return (
    <div style={styles.grid} role="list">
      {products.map((p) => (
        <div key={p.id} role="listitem" style={styles.gridItem}>
          <ProductCard
            imageUrl={p.imageUrl}
            category={p.category}
            title={p.title}
            rating={p.rating}
            ratingCount={p.ratingCount}
            price={p.price}
            href={p.href}
            isWishlisted={wishlistedSet.has(p.id)}
            onAddToCart={() => onAddToCart(p.id)}
            onToggleWishlist={() => onToggleWishlist(p.id)}
            onNavigate={onNavigate}
          />
        </div>
      ))}
    </div>
  );
}