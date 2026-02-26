import React from "react";

export default function IconToggleButton({
  active,
  ariaLabel,
  onClick = () => {},
  children,
}) {
  return (
    <button
      type="button"
      aria-label={ariaLabel}
      aria-pressed={active}
      onClick={onClick}
      className={[
        "inline-flex h-10 w-10 items-center justify-center rounded-[8px]",
        "transition-colors",
        "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#4361ee] focus-visible:ring-offset-2 focus-visible:ring-offset-white",
        active ? "bg-[#4361ee] text-white" : "bg-[#F1F5F9] text-[#64748B]",
      ].join(" ")}
    >
      {children}
    </button>
  );
}