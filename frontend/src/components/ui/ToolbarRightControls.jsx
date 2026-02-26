import React, { useMemo, useState } from "react";
import { useIntl } from "react-intl";
import SortSelectToolbarRightControls from "./SortSelectToolbarRightControls";
import ViewToggleToolbarRightControls from "./ViewToggleToolbarRightControls";

export default function ToolbarRightControls({
  sortValue: sortValueProp,
  sortOptions: sortOptionsProp,
  onSortChange = () => {},
  viewMode: viewModeProp,
  onViewModeChange = () => {},
}) {
  const intl = useIntl();

  const sortOptions = useMemo(
    () =>
      sortOptionsProp ?? [
        {
          label: intl.formatMessage({ id: "toolbarRightControls.sortOption.default" }),
          value: "default",
        },
        {
          label: intl.formatMessage({ id: "toolbarRightControls.sortOption.priceAsc" }),
          value: "price_asc",
        },
        {
          label: intl.formatMessage({ id: "toolbarRightControls.sortOption.priceDesc" }),
          value: "price_desc",
        },
        {
          label: intl.formatMessage({ id: "toolbarRightControls.sortOption.newest" }),
          value: "newest",
        },
      ],
    [intl, sortOptionsProp]
  );

  const [sortValueLocal, setSortValueLocal] = useState(
    sortValueProp ?? (sortOptions[0]?.value ?? "")
  );
  const [viewModeLocal, setViewModeLocal] = useState(viewModeProp ?? "grid");

  const sortValue = sortValueProp ?? sortValueLocal;
  const viewMode = viewModeProp ?? viewModeLocal;

  function handleSortChange(next) {
    if (sortValueProp === undefined) setSortValueLocal(next);
    onSortChange(next);
  }

  function handleViewModeChange(next) {
    if (viewModeProp === undefined) setViewModeLocal(next);
    onViewModeChange(next);
  }

  return (
    <div className="flex items-stretch gap-[20px]">
      <SortSelectToolbarRightControls
        value={sortValue}
        options={sortOptions}
        onChange={handleSortChange}
        label={intl.formatMessage({ id: "toolbarRightControls.sortLabel" })}
        placeholder=""
      />
      <ViewToggleToolbarRightControls
        value={viewMode}
        onChange={handleViewModeChange}
      />
    </div>
  );
}