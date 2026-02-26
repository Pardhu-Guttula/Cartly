export default function formatPrice(value) {
  if (typeof value === "number") return `$${value.toFixed(2)}`;
  return value?.startsWith("$") ? value : `$${value}`;
}