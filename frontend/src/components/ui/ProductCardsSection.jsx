import React from "react";
import { useIntl } from "react-intl";
import ProductCardFixed from "./ProductCardFixed";

export default function ProductCardsSection({
  products = [],
  onAddToCart = () => {},
  onNavigate = () => {},
  onToggleWishlist = () => {},
  ariaLabel,
}) {
  const intl = useIntl();

  return (
    <section
      className="w-[1040px] grid grid-cols-3 gap-3 items-start"
      aria-label={ariaLabel || intl.formatMessage({ id: "productCardsSection.ariaLabelProducts" })}
    >
      {products.map((p) => (
        <ProductCardFixed
          key={p.id}
          {...p}
          onAddToCart={onAddToCart}
          onNavigate={onNavigate}
          onToggleWishlist={onToggleWishlist}
        />
      ))}
    </section>
  );
}