const { Sequelize } = require('sequelize');

// Epic Title: Ensure Modular Architecture for Easy Integration

const sequelize = new Sequelize('mydatabase', 'username', 'password', {
  host: 'localhost',
  dialect: 'mysql',
});

module.exports = sequelize;