import React from "react";
import ResultsTextResultsSection from "./ResultsTextResultsSection";

export default function ProductsToolbarResultsText({
  shownCount = 12,
  totalCount = 20,
  className = "",
}) {
  return (
    <ResultsTextResultsSection
      shownCount={shownCount}
      totalCount={totalCount}
      className={className}
    />
  );
}