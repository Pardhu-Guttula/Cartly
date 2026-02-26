import React from "react";

export default function IconButton({
  active,
  ariaLabel,
  icon: Icon,
  onClick = () => {},
}) {
  return (
    <button
      type="button"
      aria-label={ariaLabel}
      aria-pressed={active}
      onClick={onClick}
      className={[
        "h-[40px] w-[40px] rounded-[8px] flex items-center justify-center transition",
        "focus:outline-none focus:ring-2 focus:ring-[#4361ee]/30 focus:ring-offset-2 focus:ring-offset-white",
        active
          ? "bg-[#4361ee] text-white"
          : "bg-[#F1F5F9] text-[#64748B] hover:bg-[#E2E8F0]",
      ].join(" ")}
    >
      <Icon className="h-4 w-4" />
    </button>
  );
}