import React from "react";
import { useIntl } from "react-intl";
import cx from "../utils/cx";

export default function IconToggleButton({
  active = false,
  ariaLabel = "",
  icon: Icon,
  onClick = () => {},
}) {
  useIntl();

  return (
    <button
      type="button"
      onClick={onClick}
      aria-label={ariaLabel}
      aria-pressed={active}
      className={cx(
        "h-[40px] w-[40px] rounded-[8px] flex items-center justify-center",
        "transition-colors",
        active ? "bg-[#4361ee] text-white" : "bg-[#F1F5F9] text-[#64748B]",
        "focus:outline-none focus-visible:ring-2 focus-visible:ring-[#4361ee]/30"
      )}
    >
      <Icon className="h-4 w-4" aria-hidden="true" />
    </button>
  );
}