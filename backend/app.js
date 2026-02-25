const express = require('express');
const bodyParser = require('body-parser');
const sequelize = require('./services/database');
const dataRoutes = require('./routes/dataRoutes');
const Data = require('./models/dataModel');

// Epic Title: Establish Scalable Infrastructure using Next.js, Node.js, and PostgreSQL

const app = express();
const port = 3001;

app.use(bodyParser.json());
app.use('/api', dataRoutes);

sequelize.sync().then(() => {
  console.log('Database synced');
}).catch(error => {
  console.error('Error syncing database:', error);
});

app.listen(port, () => {
  console.log(`Backend server is running on http://localhost:${port}`);
});

### PostgreSQL Database Schema