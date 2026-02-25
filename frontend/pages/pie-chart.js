import { useState, useEffect } from 'react';
import { Pie } from 'react-chartjs-2';

// Epic Title: Develop Visualization Front-end with Next.js

const PieChartPage = () => {
  const [data, setData] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    // Simulate fetching data (Normally would fetch via an API)
    try {
      const chartData = {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [
          {
            data: [300, 50, 100, 40, 120, 80],
            backgroundColor: [
              '#FF6384',
              '#36A2EB',
              '#FFCE56',
              '#4BC0C0',
              '#9966FF',
              '#FF9F40'
            ],
            hoverBackgroundColor: [
              '#FF6384',
              '#36A2EB',
              '#FFCE56',
              '#4BC0C0',
              '#9966FF',
              '#FF9F40'
            ]
          }
        ]
      };
      setData(chartData);
    } catch (e) {
      setError("Failed to load data");
    }
  }, []);

  return (
    <div style={{ padding: "20px", maxWidth: "600px", margin: "auto" }}>
      <h1>Pie Chart</h1>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {data && <Pie data={data} />}
    </div>
  );
};

export default PieChartPage;