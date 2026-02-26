import React from "react";

export default function PrimaryButton({
  label,
  iconLeft,
  onClick = () => {},
  fullWidth = true,
  disabled = false,
  style = {},
  styles = {},
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      disabled={disabled}
      style={{
        ...styles.primaryButton,
        width: fullWidth ? "100%" : "auto",
        opacity: disabled ? 0.6 : 1,
        cursor: disabled ? "not-allowed" : "pointer",
        ...style,
      }}
    >
      {iconLeft ? <span style={styles.primaryButtonIcon}>{iconLeft}</span> : null}
      <span style={styles.primaryButtonLabel}>{label}</span>
    </button>
  );
}