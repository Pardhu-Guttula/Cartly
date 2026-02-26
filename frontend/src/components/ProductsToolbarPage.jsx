import React, { useState } from "react";
import { useIntl } from "react-intl";
import ProductsToolbar from "./ui/ProductsToolbar";

export default function ProductsToolbarPage() {
  const intl = useIntl();

  const [sortValue, setSortValue] = useState("");
  const [viewMode, setViewMode] = useState("grid");

  const sortOptions = [
    {
      label: intl.formatMessage({ id: "productsToolbar.sortOption.featured" }),
      value: "featured",
    },
    {
      label: intl.formatMessage({ id: "productsToolbar.sortOption.priceAsc" }),
      value: "price_asc",
    },
    {
      label: intl.formatMessage({ id: "productsToolbar.sortOption.priceDesc" }),
      value: "price_desc",
    },
    {
      label: intl.formatMessage({ id: "productsToolbar.sortOption.newest" }),
      value: "newest",
    },
  ];

  return (
    <ProductsToolbar
      shownCount={12}
      totalCount={20}
      sortValue={sortValue}
      sortOptions={sortOptions}
      onSortChange={setSortValue}
      viewMode={viewMode}
      onViewModeChange={setViewMode}
    />
  );
}