import React from "react";
import { useIntl } from "react-intl";
import { LayoutGrid, List } from "lucide-react";
import IconToggleButton from "./IconToggleButton";

export default function ViewToggleToolbarRightControls({
  value,
  onChange = () => {},
}) {
  const intl = useIntl();

  return (
    <div className="flex items-center gap-[4px]">
      <IconToggleButton
        active={value === "grid"}
        ariaLabel={intl.formatMessage({ id: "viewToggleToolbarRightControls.gridView" })}
        onClick={() => onChange("grid")}
      >
        <LayoutGrid className="h-4 w-4" />
      </IconToggleButton>

      <IconToggleButton
        active={value === "list"}
        ariaLabel={intl.formatMessage({ id: "viewToggleToolbarRightControls.listView" })}
        onClick={() => onChange("list")}
      >
        <List className="h-4 w-4" />
      </IconToggleButton>
    </div>
  );
}