import React, { useMemo } from "react";
import { useIntl } from "react-intl";
import ProductsGridContainer from "./ui/ProductsGridContainer";

const imgFjallravenFoldsackNo1BackpackFits15Laptops =
  "https://www.figma.com/api/mcp/asset/4e86ea69-abb5-46d6-abd0-cf6253e57ca8";
const imgMensCasualPremiumSlimFitTShirts =
  "https://www.figma.com/api/mcp/asset/6922f87c-def2-4f5e-9673-5489e09073f3";
const imgMensCottonJacket =
  "https://www.figma.com/api/mcp/asset/3ab214c8-c263-40b0-9d40-6e6103e57e95";
const imgMensCasualSlimFit =
  "https://www.figma.com/api/mcp/asset/9982f626-4c0a-4129-8ce0-23b4de2d748d";
const imgJohnHardyWomensLegendsNagaGoldSilverDragonStationChainBracelet =
  "https://www.figma.com/api/mcp/asset/161d3bba-253a-4e5c-a2c2-724223cfe277";
const imgSolidGoldPetiteMicropave =
  "https://www.figma.com/api/mcp/asset/142b7635-74f4-4090-a6ff-21e13f9696f1";
const imgWhiteGoldPlatedPrincess =
  "https://www.figma.com/api/mcp/asset/1dec4f32-e322-4890-b6e2-eaadaef3cb9f";
const imgPiercedOwlRoseGoldPlatedStainlessSteelDouble =
  "https://www.figma.com/api/mcp/asset/8e1308ae-836e-40aa-817e-801f34a2aa59";
const imgWd2TbElementsPortableExternalHardDriveUsb30 =
  "https://www.figma.com/api/mcp/asset/e9f4f547-7b28-4eee-b7ff-59f69a183707";
const imgSanDiskSsdPlus1TbInternalSsdSataIii6GbS =
  "https://www.figma.com/api/mcp/asset/45779ac6-3c0a-479c-8f77-044679911aa9";
const imgSiliconPower256GbSsd3DNandA55SlcCachePerformanceBoostSataIii25 =
  "https://www.figma.com/api/mcp/asset/12601720-b695-43a6-bade-3fff126ab6c1";
const imgWd4TbGamingDriveWorksWithPlaystation4PortableExternalHardDrive =
  "https://www.figma.com/api/mcp/asset/0957fe2c-f9e2-4922-a82f-6c184094fc32";

export default function ProductsPage() {
  const intl = useIntl();

  const products = useMemo(
    () => [
      {
        id: "fjallraven-foldsack",
        imageSrc: imgFjallravenFoldsackNo1BackpackFits15Laptops,
        imageAlt: "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
        category: "men's clothing",
        title: "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
        ratingValue: 3.5,
        reviewCount: 120,
        price: "$109.95",
      },
      {
        id: "mens-casual-premium-slim-fit-tshirts",
        imageSrc: imgMensCasualPremiumSlimFitTShirts,
        imageAlt: "Mens Casual Premium Slim Fit T-Shirts",
        category: "men's clothing",
        title: "Mens Casual Premium Slim Fit T-Shirts",
        ratingValue: 4.0,
        reviewCount: 259,
        price: "$22.30",
      },
      {
        id: "mens-cotton-jacket",
        imageSrc: imgMensCottonJacket,
        imageAlt: "Mens Cotton Jacket",
        category: "men's clothing",
        title: "Mens Cotton Jacket",
        ratingValue: 4.5,
        reviewCount: 500,
        price: "$55.99",
      },
      {
        id: "mens-casual-slim-fit",
        imageSrc: imgMensCasualSlimFit,
        imageAlt: "Mens Casual Slim Fit",
        category: "men's clothing",
        title: "Mens Casual Slim Fit",
        ratingValue: 2.0,
        reviewCount: 430,
        price: "$15.99",
      },
      {
        id: "john-hardy-naga-bracelet",
        imageSrc:
          imgJohnHardyWomensLegendsNagaGoldSilverDragonStationChainBracelet,
        imageAlt:
          "John Hardy Women's Legends Naga Gold & Silver Dragon Station Chain Bracelet",
        category: "jewelery",
        title:
          "John Hardy Women's Legends Naga Gold & Silver Dragon Station Chain Bracelet",
        ratingValue: 4.5,
        reviewCount: 400,
        price: "$695.00",
      },
      {
        id: "solid-gold-petite-micropave",
        imageSrc: imgSolidGoldPetiteMicropave,
        imageAlt: "Solid Gold Petite Micropave",
        category: "jewelery",
        title: "Solid Gold Petite Micropave",
        ratingValue: 3.5,
        reviewCount: 70,
        price: "$168.00",
      },
      {
        id: "white-gold-plated-princess",
        imageSrc: imgWhiteGoldPlatedPrincess,
        imageAlt: "White Gold Plated Princess",
        category: "jewelery",
        title: "White Gold Plated Princess",
        ratingValue: 3.0,
        reviewCount: 400,
        price: "$9.99",
      },
      {
        id: "pierced-owl-rose-gold-double",
        imageSrc: imgPiercedOwlRoseGoldPlatedStainlessSteelDouble,
        imageAlt: "Pierced Owl Rose Gold Plated Stainless Steel Double",
        category: "jewelery",
        title: "Pierced Owl Rose Gold Plated Stainless Steel Double",
        ratingValue: 1.5,
        reviewCount: 100,
        price: "$10.99",
      },
      {
        id: "wd-2tb-elements",
        imageSrc: imgWd2TbElementsPortableExternalHardDriveUsb30,
        imageAlt: "WD 2TB Elements Portable External Hard Drive - USB 3.0",
        category: "electronics",
        title: "WD 2TB Elements Portable External Hard Drive - USB 3.0",
        ratingValue: 3.0,
        reviewCount: 203,
        price: "$64.00",
      },
      {
        id: "sandisk-ssd-plus-1tb",
        imageSrc: imgSanDiskSsdPlus1TbInternalSsdSataIii6GbS,
        imageAlt: "SanDisk SSD PLUS 1TB Internal SSD - SATA III 6 Gb/s",
        category: "electronics",
        title: "SanDisk SSD PLUS 1TB Internal SSD - SATA III 6 Gb/s",
        ratingValue: 2.5,
        reviewCount: 470,
        price: "$109.00",
      },
      {
        id: "silicon-power-256gb-a55",
        imageSrc:
          imgSiliconPower256GbSsd3DNandA55SlcCachePerformanceBoostSataIii25,
        imageAlt:
          "Silicon Power 256GB SSD 3D NAND A55 SLC Cache Performance Boost SATA III 2.5",
        category: "electronics",
        title:
          "Silicon Power 256GB SSD 3D NAND A55 SLC Cache Performance Boost SATA III 2.5",
        ratingValue: 4.5,
        reviewCount: 319,
        price: "$109.00",
      },
      {
        id: "wd-4tb-gaming-drive-ps4",
        imageSrc: imgWd4TbGamingDriveWorksWithPlaystation4PortableExternalHardDrive,
        imageAlt:
          "WD 4TB Gaming Drive Works with Playstation 4 Portable External Hard Drive",
        category: "electronics",
        title:
          "WD 4TB Gaming Drive Works with Playstation 4 Portable External Hard Drive",
        ratingValue: 4.5,
        reviewCount: 400,
        price: "$114.00",
      },
    ],
    []
  );

  return (
    <main className="min-h-0 bg-zinc-800 px-4 py-4 flex justify-center">
      <ProductsGridContainer
        ariaLabel={intl.formatMessage({ id: "productsGridContainer.ariaLabelProducts" })}
        products={products}
      />
    </main>
  );
}