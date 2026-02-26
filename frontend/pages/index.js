# Epic Title: Develop Visualization Front-end with Next.js

import { useState, useEffect } from 'react';
import dynamic from 'next/dynamic';

const BarChart = dynamic(() => import('../components/BarChart'), { ssr: false });
const LineChart = dynamic(() => import('../components/LineChart'), { ssr: false });
const PieChart = dynamic(() => import('../components/PieChart'), { ssr: false });

export default function Home() {
  const [chartType, setChartType] = useState('bar');
  const [data, setData] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    fetch('/api/data')
      .then(res => res.json())
      .then(setData)
      .catch(err => setError('Failed to fetch data'));
  }, []);

  return (
    <div className="container">
      <h1>Data Visualization</h1>
      {error && <p>{error}</p>}
      <div>
        <button onClick={() => setChartType('bar')}>Bar Chart</button>
        <button onClick={() => setChartType('line')}>Line Chart</button>
        <button onClick={() => setChartType('pie')}>Pie Chart</button>
      </div>
      <div className="chart">
        {chartType === 'bar' && <BarChart data={data} />}
        {chartType === 'line' && <LineChart data={data} />}
        {chartType === 'pie' && <PieChart data={data} />}
      </div>
    </div>
  );
}