import React, { useState } from "react";
import ProductsToolbar from "./layout/ProductsToolbar";

export default function ProductsToolbarPage() {
  const [sortValue, setSortValue] = useState("");
  const [viewMode, setViewMode] = useState("grid");

  const showingCount = 12;
  const totalCount = 20;

  const sortOptions = [
    { label: "Default", value: "" },
    { label: "Price: Low to High", value: "price_asc" },
    { label: "Price: High to Low", value: "price_desc" },
    { label: "Newest", value: "newest" },
  ];

  return (
    <div className="w-full">
      <ProductsToolbar
        showingCount={showingCount}
        totalCount={totalCount}
        sortValue={sortValue}
        sortOptions={sortOptions}
        onSortChange={setSortValue}
        viewMode={viewMode}
        onViewModeChange={setViewMode}
      />
    </div>
  );
}