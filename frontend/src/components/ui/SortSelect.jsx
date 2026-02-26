import React from "react";
import { useIntl } from "react-intl";

export default function SortSelect({
  id,
  value,
  options,
  onChange = () => {},
  placeholder = "",
}) {
  const intl = useIntl();

  return (
    <div className="flex items-center gap-[10px]">
      <label
        htmlFor={id}
        className="text-[14px] leading-[22.4px] text-[#475569] whitespace-nowrap"
      >
        {intl.formatMessage({ id: "sortSelect.label" })}
      </label>

      <div className="relative">
        <select
          id={id}
          value={value}
          onChange={(e) => onChange(e.target.value)}
          className="h-[41px] w-[156.5px] appearance-none rounded-[8px] border border-[#CBD5E1] bg-white px-3 pr-9 text-[14px] leading-[22.4px] text-[#475569] outline-none transition focus:border-[#4361ee] focus:ring-2 focus:ring-[#4361ee]/20"
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
          <path
            fillRule="evenodd"
            d="M5.23 7.21a.75.75 0 0 1 1.06.02L10 10.94l3.71-3.71a.75.75 0 1 1 1.06 1.06l-4.24 4.24a.75.75 0 0 1-1.06 0L5.21 8.29a.75.75 0 0 1 .02-1.08z"
            clipRule="evenodd"
          />
        </svg>
      </div>
    </div>
  );
}