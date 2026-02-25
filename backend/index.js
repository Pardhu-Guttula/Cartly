const express = require('express');
const bodyParser = require('body-parser');
const sequelize = require('./services/database');
const orderRoutes = require('./routes/order');
const Promotion = require('./models/promotion');
const Order = require('./models/order');

const app = express();
const port = 3000;

// Epic Title: Integrate Promotion System with Order Management

app.use(bodyParser.json());

app.use('/api/orders', orderRoutes);

sequelize.sync().then(async () => {
  console.log('Database synced');
}).catch(error => {
  console.error('Error syncing database:', error);
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

### Database Schema
Below is the SQL for the database schema: