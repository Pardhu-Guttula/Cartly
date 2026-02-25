const { Sequelize } = require('sequelize');

// Epic Title: Integrate Promotion System with Order Management

const sequelize = new Sequelize('mydatabase', 'username', 'password', {
  host: 'localhost',
  dialect: 'mysql',
});

module.exports = sequelize;