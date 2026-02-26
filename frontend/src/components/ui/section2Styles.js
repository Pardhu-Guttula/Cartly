const section2Styles = {
  grid: {
    width: "100%",
    display: "grid",
    gridTemplateColumns: "repeat(3, minmax(0, 1fr))",
    gap: 24,
  },

  card: {
    backgroundColor: "#FFFFFF",
    borderRadius: 16,
    overflow: "hidden",
    border: "1px solid rgba(15, 23, 42, 0.08)",
    display: "flex",
    flexDirection: "column",
    minHeight: 520,
    transition: "box-shadow 160ms ease, transform 160ms ease",
  },
  cardShadow: "0px 1px 3px rgba(0,0,0,0.10), 0px 1px 2px rgba(0,0,0,0.06)",
  cardShadowHover: "0px 10px 20px rgba(0,0,0,0.10), 0px 4px 8px rgba(0,0,0,0.06)",

  imageWrap: {
    height: 280,
    backgroundColor: "#F8FAFC",
    padding: 24,
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  },
  image: {
    maxHeight: 224,
    maxWidth: 264.53,
    width: "auto",
    height: "auto",
    objectFit: "contain",
    display: "block",
  },

  body: {
    paddingLeft: 20,
    paddingRight: 20,
    paddingTop: 24.25,
    paddingBottom: 20,
    display: "flex",
    flexDirection: "column",
    gap: 1.4,
    flex: 1,
  },

  category: {
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Roboto, sans-serif",
    fontWeight: 600,
    fontSize: 12,
    lineHeight: "19.2px",
    letterSpacing: "0.5px",
    textTransform: "uppercase",
    color: "#4361EE",
    whiteSpace: "nowrap",
  },

  titleLink: {
    textDecoration: "none",
    color: "inherit",
    display: "block",
  },
  titleClamp: {
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Roboto, sans-serif",
    fontWeight: 600,
    fontSize: 15,
    lineHeight: "21px",
    color: "#1E293B",
    display: "-webkit-box",
    WebkitLineClamp: 2,
    WebkitBoxOrient: "vertical",
    overflow: "hidden",
    minHeight: 42,
  },

  ratingRow: {
    display: "flex",
    alignItems: "center",
    gap: 8,
    paddingTop: 8.6,
  },
  starsRow: {
    display: "flex",
    alignItems: "center",
    gap: 2,
    paddingTop: 3.5,
    paddingBottom: 4.3,
  },
  starIcon: {
    flex: "0 0 auto",
  },
  ratingCount: {
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Roboto, sans-serif",
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
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Roboto, sans-serif",
    fontWeight: 700,
    fontSize: 20,
    lineHeight: "32px",
    color: "#4361EE",
  },

  addBtn: {
    marginTop: "auto",
    width: "100%",
    border: "none",
    borderRadius: 8,
    padding: 12,
    display: "inline-flex",
    alignItems: "center",
    justifyContent: "center",
    gap: 8,
    cursor: "pointer",
    transition: "background-color 160ms ease, transform 120ms ease",
  },
  addBtnLabel: {
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, Roboto, sans-serif",
    fontWeight: 600,
    fontSize: 14,
    lineHeight: "normal",
    color: "#FFFFFF",
  },
};

export default section2Styles;