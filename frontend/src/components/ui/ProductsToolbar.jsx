import React, { useId, useState } from "react";
import SortSelect from "./SortSelect";
import ViewToggle from "./ViewToggle";
import ResultsText from "./ResultsText";

export default function ProductsToolbar({
  shownCount = 12,
  totalCount = 20,
  sortValue: sortValueProp,
  sortOptions = [
    { label: "Featured", value: "featured" },
    { label: "Price: Low to High", value: "price_asc" },
    { label: "Price: High to Low", value: "price_desc" },
    { label: "Newest", value: "newest" },
  ],
  onSortChange = () => {},
  viewMode: viewModeProp,
  onViewModeChange = () => {},
}) {
  const sortId = useId();

  const [sortValueLocal, setSortValueLocal] = useState(sortValueProp ?? "");
  const [viewModeLocal, setViewModeLocal] = useState(viewModeProp ?? "grid");

  const sortValue = sortValueProp ?? sortValueLocal;
  const viewMode = viewModeProp ?? viewModeLocal;

  return (
    <div className="w-full">
      <div className="flex min-h-[73px] w-full items-center justify-between gap-6 rounded-[12px] bg-white px-[20px] py-[16px] shadow-[0px_1px_3px_0px_rgba(0,0,0,0.1),0px_1px_2px_0px_rgba(0,0,0,0.06)]">
        <div className="flex flex-col items-start">
          <ResultsText shownCount={shownCount} totalCount={totalCount} />
        </div>

        <div className="flex items-center gap-[20px]">
          <SortSelect
            id={sortId}
            value={sortValue}
            options={sortOptions}
            placeholder=""
            onChange={(next) => {
              setSortValueLocal(next);
              onSortChange(next);
            }}
          />

          <ViewToggle
            value={viewMode}
            onChange={(mode) => {
              setViewModeLocal(mode);
              onViewModeChange(mode);
            }}
          />
        </div>
      </div>
    </div>
  );
}