const styles = {
  container: {
    width: 1040,
    maxWidth: "100%",
    margin: "0 auto",
  },

  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(3, minmax(0, 1fr))",
    gap: 24,
    alignItems: "stretch",
  },
  gridItem: {
    minWidth: 0,
  },

  card: {
    backgroundColor: "#FFFFFF",
    borderRadius: 16,
    overflow: "hidden",
    boxShadow: "0px 1px 3px rgba(0,0,0,0.10), 0px 1px 2px rgba(0,0,0,0.06)",
    display: "flex",
    flexDirection: "column",
    height: "100%",
  },

  imageArea: {
    backgroundColor: "#F8FAFC",
    height: 280,
    padding: 24,
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    position: "relative",
  },
  productImage: {
    maxHeight: 224,
    maxWidth: 264.53,
    width: "auto",
    height: "auto",
    objectFit: "contain",
    display: "block",
  },

  actionsOverlay: {
    position: "absolute",
    top: 16,
    right: 6,
    display: "flex",
    flexDirection: "column",
    gap: 8,
    transition: "opacity 160ms ease, transform 160ms ease",
  },
  wishlistButton: {
    width: 40,
    height: 40,
    borderRadius: 9999,
    border: "none",
    backgroundColor: "#FFFFFF",
    boxShadow: "0px 4px 6px -1px rgba(0,0,0,0.10), 0px 2px 4px -1px rgba(0,0,0,0.06)",
    display: "inline-flex",
    alignItems: "center",
    justifyContent: "center",
    cursor: "pointer",
  },

  body: {
    paddingLeft: 20,
    paddingRight: 20,
    paddingTop: 24.25,
    paddingBottom: 20,
    display: "flex",
    flexDirection: "column",
    gap: 1.4,
    flex: "1 1 auto",
  },

  category: {
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif",
    fontWeight: 600,
    fontSize: 12,
    lineHeight: "19.2px",
    letterSpacing: "0.5px",
    textTransform: "uppercase",
    color: "#4361EE",
    whiteSpace: "nowrap",
  },

  title: {
    margin: 0,
    minHeight: 42,
    overflow: "hidden",
    display: "-webkit-box",
    WebkitLineClamp: 2,
    WebkitBoxOrient: "vertical",
  },
  titleLink: {
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif",
    fontWeight: 600,
    fontSize: 15,
    lineHeight: "21px",
    color: "#1E293B",
    textDecoration: "none",
    display: "inline",
  },

  ratingRow: {
    display: "flex",
    alignItems: "center",
    gap: 8,
    paddingTop: 8.6,
  },
  starsRow: {
    display: "inline-flex",
    alignItems: "center",
    gap: 2,
    paddingTop: 3.5,
    paddingBottom: 4.3,
  },
  starIcon: {
    display: "block",
  },
  ratingCount: {
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif",
    fontWeight: 400,
    fontSize: 13,
    lineHeight: "20.8px",
    color: "#64748B",
    whiteSpace: "nowrap",
  },

  priceRow: {
    display: "flex",
    alignItems: "center",
    paddingTop: 10.59,
    paddingBottom: 14.6,
  },
  price: {
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif",
    fontWeight: 700,
    fontSize: 20,
    lineHeight: "32px",
    color: "#4361EE",
  },

  ctaRow: {
    marginTop: "auto",
  },
  primaryButton: {
    backgroundColor: "#4361EE",
    border: "none",
    borderRadius: 8,
    padding: 12,
    display: "inline-flex",
    alignItems: "center",
    justifyContent: "center",
    gap: 8,
    height: 44,
  },
  primaryButtonIcon: {
    display: "inline-flex",
    alignItems: "center",
    justifyContent: "center",
  },
  primaryButtonLabel: {
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif",
    fontWeight: 600,
    fontSize: 14,
    lineHeight: "normal",
    color: "#FFFFFF",
    whiteSpace: "nowrap",
  },
};

export default styles;