import React, { useMemo } from "react";
import { useIntl } from "react-intl";
import { LayoutGrid, List } from "lucide-react";
import IconButton from "./IconButton";

export default function ViewToggle({ value, onChange = () => {} }) {
  const intl = useIntl();

  const items = useMemo(
    () => [
      {
        mode: "grid",
        ariaLabel: intl.formatMessage({ id: "viewToggle.gridView" }),
        icon: LayoutGrid,
      },
      {
        mode: "list",
        ariaLabel: intl.formatMessage({ id: "viewToggle.listView" }),
        icon: List,
      },
    ],
    [intl]
  );

  return (
    <div className="flex items-center gap-[4px]">
      {items.map((item) => (
        <IconButton
          key={item.mode}
          active={value === item.mode}
          ariaLabel={item.ariaLabel}
          icon={item.icon}
          onClick={() => onChange(item.mode)}
        />
      ))}
    </div>
  );
}