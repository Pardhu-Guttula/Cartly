const express = require('express');
const bodyParser = require('body-parser');
const sequelize = require('./services/database');
const Data = require('./models/data');
const routes = require('./routes/index');

// Epic Title: Develop Data Processing Backend with Node.js

const app = express();
const port = 3000;

app.use(bodyParser.json());
app.use('/api', routes);

sequelize.sync().then(async () => {
  console.log('Database synced');
}).catch(error => {
  console.error('Error syncing database:', error);
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});