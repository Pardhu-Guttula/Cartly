const express = require('express');
const bodyParser = require('body-parser');
const sequelize = require('./services/database');
const userRoutes = require('./routes/userRoutes');
const productRoutes = require('./routes/productRoutes');
const orderRoutes = require('./routes/orderRoutes');

// Epic Title: Ensure Modular Architecture for Easy Integration

const app = express();
const port = 3000;

app.use(bodyParser.json());

app.use('/api', userRoutes);
app.use('/api', productRoutes);
app.use('/api', orderRoutes);

sequelize.sync().then(() => {
  console.log('Database synced');
}).catch(error => {
  console.error('Error syncing database:', error);
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

### Database Schema