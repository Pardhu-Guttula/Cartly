import React from "react";
import { useIntl } from "react-intl";

export default function ResultsTextResultsSection({
  shownCount = 12,
  totalCount = 20,
  className = "",
}) {
  const intl = useIntl();

  return (
    <span
      className={[
        "flex flex-col items-start",
        "text-[14px] leading-[22.4px] text-[#475569]",
        "font-['Inter',sans-serif]",
        className,
      ].join(" ")}
      aria-live="polite"
    >
      <span className="whitespace-nowrap">
        <span className="font-normal">
          {intl.formatMessage({ id: "resultsTextResultsSection.showingPrefix" })}{" "}
        </span>
        <span className="font-bold">{shownCount}</span>
        <span className="font-normal">
          {" "}
          {intl.formatMessage({ id: "resultsTextResultsSection.of" })}{" "}
        </span>
        <span className="font-bold">{totalCount}</span>
        <span className="font-normal">
          {" "}
          {intl.formatMessage({
            id: "resultsTextResultsSection.productsSuffix",
          })}
        </span>
      </span>
    </span>
  );
}