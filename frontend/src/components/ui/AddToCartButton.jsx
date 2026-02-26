import React from "react";
import { useIntl } from "react-intl";
import { ShoppingCart } from "lucide-react";

export default function AddToCartButton({ onClick = () => {}, disabled = false }) {
  const intl = useIntl();

  return (
    <button
      type="button"
      onClick={onClick}
      disabled={disabled}
      style={{
        width: "100%",
        border: 0,
        borderRadius: 8,
        background: disabled ? "#94A3B8" : "#4361EE",
        color: "#FFFFFF",
        padding: 12,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        gap: 8,
        cursor: disabled ? "not-allowed" : "pointer",
        fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Roboto, sans-serif",
        fontSize: 14,
        fontWeight: 600,
        lineHeight: "normal",
      }}
    >
      <ShoppingCart size={14} />
      <span>{intl.formatMessage({ id: "addToCartButton.label" })}</span>
    </button>
  );
}