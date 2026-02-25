const { Sequelize } = require('sequelize');

// Epic Title: Develop Data Processing Backend with Node.js

const sequelize = new Sequelize('mydatabase', 'username', 'password', {
  host: 'localhost',
  dialect: 'mysql',
});

module.exports = sequelize;

### Database Schema