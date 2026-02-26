import React from "react";
import ProductsGridContainer from "./ui/ProductsGridContainer";

export default function ProductsGridPage() {
  return (
    <main
      style={{
        minHeight: "100vh",
        background: "#F8FAFC",
        padding: 24,
        display: "flex",
        justifyContent: "center",
      }}
    >
      <ProductsGridContainer
        onProductClick={(id) => {
          // no-op
        }}
        onAddToCart={(id) => {
          // no-op
        }}
      />
    </main>
  );
}