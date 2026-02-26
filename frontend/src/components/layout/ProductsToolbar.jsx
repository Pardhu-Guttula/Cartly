import React from "react";
import { useIntl } from "react-intl";
import ResultsText from "../ui/ResultsText";
import SortControl from "../ui/SortControl";
import ViewToggle from "../ui/ViewToggle";

export default function ProductsToolbar({
  showingCount = 12,
  totalCount = 20,
  sortValue = "",
  sortOptions = [
    { label: "Default", value: "" },
    { label: "Price: Low to High", value: "price_asc" },
    { label: "Price: High to Low", value: "price_desc" },
    { label: "Newest", value: "newest" },
  ],
  onSortChange = () => {},
  viewMode = "grid",
  onViewModeChange = () => {},
}) {
  const intl = useIntl();

  return (
    <header className="w-full">
      <section
        className={[
          "w-full rounded-[12px] bg-white shadow-[0px_1px_3px_0px_rgba(0,0,0,0.1),0px_1px_2px_0px_rgba(0,0,0,0.06)]",
          "px-[20px] py-[16px]",
          "flex items-center justify-between gap-4",
          "flex-wrap sm:flex-nowrap",
        ].join(" ")}
        aria-label="Products toolbar"
      >
        <div className="flex flex-col items-start">
          <ResultsText showingCount={showingCount} totalCount={totalCount} />
        </div>

        <div className="flex items-center gap-[20px]">
          <SortControl
            value={sortValue}
            options={sortOptions}
            onChange={onSortChange}
            label={intl.formatMessage({ id: "productsToolbar.sortLabel" })}
          />
          <ViewToggle value={viewMode} onChange={onViewModeChange} />
        </div>
      </section>
    </header>
  );
}