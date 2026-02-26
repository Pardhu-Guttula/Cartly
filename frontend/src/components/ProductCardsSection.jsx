import React, { useMemo } from "react";
import { useIntl } from "react-intl";
import Section2ProductCard from "./ui/Section2ProductCard";
import section2Styles from "./ui/section2Styles";

const imgFjallravenFoldsackNo1BackpackFits15Laptops =
  "https://www.figma.com/api/mcp/asset/a10e0955-7c4f-4911-9991-cfd7c7babbce";
const imgMensCasualPremiumSlimFitTShirts =
  "https://www.figma.com/api/mcp/asset/4bb7149c-5274-4f05-b2a8-4e8a3cb3601f";
const imgMensCottonJacket =
  "https://www.figma.com/api/mcp/asset/876af512-5354-49e6-b59f-6aab4c3e28f3";
const imgMensCasualSlimFit =
  "https://www.figma.com/api/mcp/asset/0a27f147-eb46-495f-bd57-2559ea692aa6";
const imgJohnHardyWomensLegendsNagaGoldSilverDragonStationChainBracelet =
  "https://www.figma.com/api/mcp/asset/299a7385-67fc-4781-ab97-d95958a69879";
const imgSolidGoldPetiteMicropave =
  "https://www.figma.com/api/mcp/asset/e6a9518a-4363-462a-986c-fa073619e6f8";
const imgWhiteGoldPlatedPrincess =
  "https://www.figma.com/api/mcp/asset/53940a67-53b8-4de5-9838-2c07e04cc825";
const imgPiercedOwlRoseGoldPlatedStainlessSteelDouble =
  "https://www.figma.com/api/mcp/asset/92b54a07-3f52-47ed-a7e1-9ad8249d36a7";
const imgWd2TbElementsPortableExternalHardDriveUsb30 =
  "https://www.figma.com/api/mcp/asset/89fcc47c-b690-4843-aae9-4aa0fdacd249";
const imgSanDiskSsdPlus1TbInternalSsdSataIii6GbS =
  "https://www.figma.com/api/mcp/asset/88e054cd-0231-4d6d-b62c-1c480725037c";
const imgSiliconPower256GbSsd3DNandA55SlcCachePerformanceBoostSataIii25 =
  "https://www.figma.com/api/mcp/asset/39275dfa-1153-49a6-b678-50eba1d05d06";
const imgWd4TbGamingDriveWorksWithPlaystation4PortableExternalHardDrive =
  "https://www.figma.com/api/mcp/asset/aeba2705-dd26-476b-9651-09ba5df41820";

export default function ProductCardsSection({ onAddToCart = () => {}, onProductClick = () => {} }) {
  const intl = useIntl();

  const products = useMemo(
    () => [
      {
        id: "p1",
        imageUrl: imgFjallravenFoldsackNo1BackpackFits15Laptops,
        category: intl.formatMessage({ id: "products.category.mensClothing" }),
        title: intl.formatMessage({ id: "products.title.p1" }),
        rating: 4,
        ratingCount: 120,
        price: "$109.95",
      },
      {
        id: "p2",
        imageUrl: imgMensCasualPremiumSlimFitTShirts,
        category: intl.formatMessage({ id: "products.category.mensClothing" }),
        title: intl.formatMessage({ id: "products.title.p2" }),
        rating: 4,
        ratingCount: 259,
        price: "$22.30",
      },
      {
        id: "p3",
        imageUrl: imgMensCottonJacket,
        category: intl.formatMessage({ id: "products.category.mensClothing" }),
        title: intl.formatMessage({ id: "products.title.p3" }),
        rating: 4,
        ratingCount: 500,
        price: "$55.99",
      },
      {
        id: "p4",
        imageUrl: imgMensCasualSlimFit,
        category: intl.formatMessage({ id: "products.category.mensClothing" }),
        title: intl.formatMessage({ id: "products.title.p4" }),
        rating: 2,
        ratingCount: 430,
        price: "$15.99",
      },
      {
        id: "p5",
        imageUrl: imgJohnHardyWomensLegendsNagaGoldSilverDragonStationChainBracelet,
        category: intl.formatMessage({ id: "products.category.jewelery" }),
        title: intl.formatMessage({ id: "products.title.p5" }),
        rating: 4,
        ratingCount: 400,
        price: "$695.00",
      },
      {
        id: "p6",
        imageUrl: imgSolidGoldPetiteMicropave,
        category: intl.formatMessage({ id: "products.category.jewelery" }),
        title: intl.formatMessage({ id: "products.title.p6" }),
        rating: 4,
        ratingCount: 70,
        price: "$168.00",
      },
      {
        id: "p7",
        imageUrl: imgWhiteGoldPlatedPrincess,
        category: intl.formatMessage({ id: "products.category.jewelery" }),
        title: intl.formatMessage({ id: "products.title.p7" }),
        rating: 3,
        ratingCount: 400,
        price: "$9.99",
      },
      {
        id: "p8",
        imageUrl: imgPiercedOwlRoseGoldPlatedStainlessSteelDouble,
        category: intl.formatMessage({ id: "products.category.jewelery" }),
        title: intl.formatMessage({ id: "products.title.p8" }),
        rating: 2,
        ratingCount: 100,
        price: "$10.99",
      },
      {
        id: "p9",
        imageUrl: imgWd2TbElementsPortableExternalHardDriveUsb30,
        category: intl.formatMessage({ id: "products.category.electronics" }),
        title: intl.formatMessage({ id: "products.title.p9" }),
        rating: 3,
        ratingCount: 203,
        price: "$64.00",
      },
      {
        id: "p10",
        imageUrl: imgSanDiskSsdPlus1TbInternalSsdSataIii6GbS,
        category: intl.formatMessage({ id: "products.category.electronics" }),
        title: intl.formatMessage({ id: "products.title.p10" }),
        rating: 3,
        ratingCount: 470,
        price: "$109.00",
      },
      {
        id: "p11",
        imageUrl: imgSiliconPower256GbSsd3DNandA55SlcCachePerformanceBoostSataIii25,
        category: intl.formatMessage({ id: "products.category.electronics" }),
        title: intl.formatMessage({ id: "products.title.p11" }),
        rating: 4,
        ratingCount: 319,
        price: "$109.00",
      },
      {
        id: "p12",
        imageUrl: imgWd4TbGamingDriveWorksWithPlaystation4PortableExternalHardDrive,
        category: intl.formatMessage({ id: "products.category.electronics" }),
        title: intl.formatMessage({ id: "products.title.p12" }),
        rating: 4,
        ratingCount: 400,
        price: "$114.00",
      },
    ],
    [intl]
  );

  return (
    <div style={section2Styles.grid}>
      {products.map((p) => (
        <Section2ProductCard
          key={p.id}
          imageUrl={p.imageUrl}
          category={p.category}
          title={p.title}
          rating={p.rating}
          ratingCount={p.ratingCount}
          price={p.price}
          onProductClick={(e) => onProductClick(p.id, e)}
          onAddToCart={() => onAddToCart(p.id)}
        />
      ))}
    </div>
  );
}