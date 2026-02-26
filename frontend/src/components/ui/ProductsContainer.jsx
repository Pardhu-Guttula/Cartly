import React, { useMemo } from "react";
import ProductCardSection2 from "./ProductCardSection2";

const imgFjallravenFoldsackNo1BackpackFits15Laptops =
  "https://www.figma.com/api/mcp/asset/25db0ce6-0337-42f9-a7fb-4455b23533ad";
const imgMensCasualPremiumSlimFitTShirts =
  "https://www.figma.com/api/mcp/asset/f6c15ca0-efd8-4825-84bb-1ee51d45d6e3";
const imgMensCottonJacket =
  "https://www.figma.com/api/mcp/asset/cb2302e5-7837-4b62-809a-4363ae0c2623";
const imgMensCasualSlimFit =
  "https://www.figma.com/api/mcp/asset/c867dd9f-5298-40eb-910b-29c6e430cc61";
const imgJohnHardyWomensLegendsNagaGoldSilverDragonStationChainBracelet =
  "https://www.figma.com/api/mcp/asset/c6319418-5df6-4b3f-9f57-609ba854a343";
const imgSolidGoldPetiteMicropave =
  "https://www.figma.com/api/mcp/asset/691d41e9-a16f-4c82-978f-4b99ea75da47";
const imgWhiteGoldPlatedPrincess =
  "https://www.figma.com/api/mcp/asset/09e7a1d5-2e94-44d9-90ac-f1d622f52653";
const imgPiercedOwlRoseGoldPlatedStainlessSteelDouble =
  "https://www.figma.com/api/mcp/asset/a853e846-c35f-4e51-88ed-3bd6eab0f9c7";
const imgWd2TbElementsPortableExternalHardDriveUsb30 =
  "https://www.figma.com/api/mcp/asset/1535d40c-ef69-4861-a1c1-b6f838122583";
const imgSanDiskSsdPlus1TbInternalSsdSataIii6GbS =
  "https://www.figma.com/api/mcp/asset/526a156a-7928-4db4-bb9a-42068a39c98a";
const imgSiliconPower256GbSsd3DNandA55SlcCachePerformanceBoostSataIii25 =
  "https://www.figma.com/api/mcp/asset/52fcf07b-d915-4770-bf40-1bc067e1e0b4";
const imgWd4TbGamingDriveWorksWithPlaystation4PortableExternalHardDrive =
  "https://www.figma.com/api/mcp/asset/42a57b52-1ff6-4ca3-82de-2e823a333a35";

export default function ProductsContainer({ onAddToCart = () => {}, onProductClick = () => {} }) {
  const products = useMemo(
    () => [
      {
        id: "p1",
        imageUrl: imgFjallravenFoldsackNo1BackpackFits15Laptops,
        category: "men's clothing",
        title: "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
        rating: 3.5,
        ratingCount: 120,
        price: "$109.95",
      },
      {
        id: "p2",
        imageUrl: imgMensCasualPremiumSlimFitTShirts,
        category: "men's clothing",
        title: "Mens Casual Premium Slim Fit T-Shirts",
        rating: 4,
        ratingCount: 259,
        price: "$22.30",
      },
      {
        id: "p3",
        imageUrl: imgMensCottonJacket,
        category: "men's clothing",
        title: "Mens Cotton Jacket",
        rating: 4.5,
        ratingCount: 500,
        price: "$55.99",
      },
      {
        id: "p4",
        imageUrl: imgMensCasualSlimFit,
        category: "men's clothing",
        title: "Mens Casual Slim Fit",
        rating: 2,
        ratingCount: 430,
        price: "$15.99",
      },
      {
        id: "p5",
        imageUrl: imgJohnHardyWomensLegendsNagaGoldSilverDragonStationChainBracelet,
        category: "jewelery",
        title: "John Hardy Women's Legends Naga Gold & Silver Dragon Station Chain Bracelet",
        rating: 4.5,
        ratingCount: 400,
        price: "$695.00",
      },
      {
        id: "p6",
        imageUrl: imgSolidGoldPetiteMicropave,
        category: "jewelery",
        title: "Solid Gold Petite Micropave",
        rating: 3.5,
        ratingCount: 70,
        price: "$168.00",
      },
      {
        id: "p7",
        imageUrl: imgWhiteGoldPlatedPrincess,
        category: "jewelery",
        title: "White Gold Plated Princess",
        rating: 3,
        ratingCount: 400,
        price: "$9.99",
      },
      {
        id: "p8",
        imageUrl: imgPiercedOwlRoseGoldPlatedStainlessSteelDouble,
        category: "jewelery",
        title: "Pierced Owl Rose Gold Plated Stainless Steel Double",
        rating: 1.5,
        ratingCount: 100,
        price: "$10.99",
      },
      {
        id: "p9",
        imageUrl: imgWd2TbElementsPortableExternalHardDriveUsb30,
        category: "electronics",
        title: "WD 2TB Elements Portable External Hard Drive - USB 3.0",
        rating: 3,
        ratingCount: 203,
        price: "$64.00",
      },
      {
        id: "p10",
        imageUrl: imgSanDiskSsdPlus1TbInternalSsdSataIii6GbS,
        category: "electronics",
        title: "SanDisk SSD PLUS 1TB Internal SSD - SATA III 6 Gb/s",
        rating: 2.5,
        ratingCount: 470,
        price: "$109.00",
      },
      {
        id: "p11",
        imageUrl: imgSiliconPower256GbSsd3DNandA55SlcCachePerformanceBoostSataIii25,
        category: "electronics",
        title: "Silicon Power 256GB SSD 3D NAND A55 SLC Cache Performance Boost SATA III 2.5",
        rating: 4.5,
        ratingCount: 319,
        price: "$109.00",
      },
      {
        id: "p12",
        imageUrl: imgWd4TbGamingDriveWorksWithPlaystation4PortableExternalHardDrive,
        category: "electronics",
        title: "WD 4TB Gaming Drive Works with Playstation 4 Portable External Hard Drive",
        rating: 4.5,
        ratingCount: 400,
        price: "$114.00",
      },
    ],
    []
  );

  return (
    <div
      style={{
        width: 1040,
        display: "grid",
        gridTemplateColumns: "repeat(3, minmax(0, 1fr))",
        gap: 24,
      }}
    >
      {products.map((p) => (
        <ProductCardSection2
          key={p.id}
          imageUrl={p.imageUrl}
          category={p.category}
          title={p.title}
          rating={p.rating}
          ratingCount={p.ratingCount}
          price={p.price}
          onAddToCart={() => onAddToCart(p.id)}
          onProductClick={() => onProductClick(p.id)}
        />
      ))}
    </div>
  );
}