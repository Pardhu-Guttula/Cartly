# Epic Title: Develop Visualization Front-end with Next.js

import { Line } from 'react-chartjs-2';

const LineChart = ({ data }) => {
  const chartData = {
    labels: data.map(d => d.label),
    datasets: [
      {
        label: 'Value',
        data: data.map(d => d.value),
        borderColor: 'rgba(75, 192, 192, 0.6)',
        fill: false,
      },
    ],
  };

  return <Line data={chartData} />;
};

export default LineChart;