import { useState } from 'react';
import Link from 'next/link';

// Epic Title: Develop Visualization Front-end with Next.js

const Home = () => {
  return (
    <div style={{ padding: "20px", maxWidth: "600px", margin: "auto" }}>
      <h1>Data Visualization Tool</h1>
      <nav>
        <ul>
          <li><Link href="/bar-chart"><a>Bar Chart</a></Link></li>
          <li><Link href="/line-chart"><a>Line Chart</a></Link></li>
          <li><Link href="/pie-chart"><a>Pie Chart</a></Link></li>
        </ul>
      </nav>
    </div>
  );
};

export default Home;