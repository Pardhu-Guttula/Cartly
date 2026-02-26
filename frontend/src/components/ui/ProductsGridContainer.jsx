import React from "react";
import { useIntl } from "react-intl";
import ProductCard from "./ProductCard";

export default function ProductsGridContainer({
  products = [],
  onAddToCart = () => {},
  onNavigate = () => {},
  onToggleWishlist = () => {},
  onRate = () => {},
  ariaLabel,
}) {
  const intl = useIntl();

  return (
    <section
      data-node-id="1839:4491"
      className="w-[1040px] max-w-full bg-transparent p-0 rounded-none"
      aria-label={ariaLabel || intl.formatMessage({ id: "productsGridContainer.ariaLabelProducts" })}
    >
      <div className="grid grid-cols-3 gap-3">
        {products.map((p) => (
          <ProductCard
            key={p.id}
            {...p}
            onNavigate={(id) => onNavigate(id)}
            onAddToCart={(id) => onAddToCart(id)}
            onToggleWishlist={(id, next) => onToggleWishlist(id, next)}
            onRate={(id, stars) => onRate(id, stars)}
          />
        ))}
      </div>

      <style>{`
        @media (max-width: 1100px) {
          [data-node-id="1839:4491"] > div {
            grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
          }
        }
        @media (max-width: 900px) {
          [data-node-id="1839:4491"] > div {
            grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
          }
        }
        @media (max-width: 640px) {
          [data-node-id="1839:4491"] {
            padding: 0 !important;
          }
          [data-node-id="1839:4491"] > div {
            grid-template-columns: 1fr !important;
            gap: 12px !important;
          }
        }
      `}</style>
    </section>
  );
}