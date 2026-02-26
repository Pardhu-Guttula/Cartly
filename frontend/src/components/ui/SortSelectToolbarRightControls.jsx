import React, { useId } from "react";
import { useIntl } from "react-intl";

export default function SortSelectToolbarRightControls({
  value,
  options,
  onChange = () => {},
  label,
  placeholder = "",
}) {
  const intl = useIntl();
  const selectId = useId();

  const computedLabel =
    label ?? intl.formatMessage({ id: "sortSelectToolbarRightControls.label" });

  return (
    <div className="flex items-center justify-center gap-[10px]">
      <label
        htmlFor={selectId}
        className="text-[14px] leading-[22.4px] text-[#475569]"
      >
        {computedLabel}
      </label>

      <div className="relative">
        <select
          id={selectId}
          value={value}
          onChange={(e) => onChange(e.target.value)}
          className={[
            "h-[41px] w-[156.5px] rounded-[8px] border border-[#CBD5E1] bg-white",
            "px-3 pr-9 text-[14px] leading-[22.4px] text-[#475569]",
            "appearance-none",
            "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#4361ee] focus-visible:ring-offset-2 focus-visible:ring-offset-white",
          ].join(" ")}
        >
          {placeholder !== null && (
            <option value="" disabled={false}>
              {placeholder}
            </option>
          )}
          {options.map((opt) => (
            <option key={opt.value} value={opt.value}>
              {opt.label}
            </option>
          ))}
        </select>

        <svg
          aria-hidden="true"
          viewBox="0 0 20 20"
          className="pointer-events-none absolute right-3 top-1/2 h-4 w-4 -translate-y-1/2 text-[#64748B]"
          fill="currentColor"
        >
          <path d="M5.5 7.5a1 1 0 0 1 1.6-.8L10 9.2l2.9-2.5a1 1 0 1 1 1.3 1.5l-3.6 3.1a1 1 0 0 1-1.3 0L5.7 8.2a1 1 0 0 1-.2-.7Z" />
        </svg>
      </div>
    </div>
  );
}