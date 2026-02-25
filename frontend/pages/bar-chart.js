import { useState, useEffect } from 'react';
import { Bar } from 'react-chartjs-2';

// Epic Title: Develop Visualization Front-end with Next.js

const BarChartPage = () => {
  const [data, setData] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    // Simulate fetching data (Normally would fetch via an API)
    try {
      const chartData = {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [
          {
            label: 'Sales',
            backgroundColor: 'rgba(75,192,192,1)',
            borderColor: 'rgba(0,0,0,0.1)',
            borderWidth: 1,
            hoverBackgroundColor: 'rgba(75,192,192,0.4)',
            hoverBorderColor: 'rgba(0,0,0,1)',
            data: [65, 59, 80, 81, 56, 55, 40]
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
      <h1>Bar Chart</h1>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {data && <Bar data={data} />}
    </div>
  );
};

export default BarChartPage;