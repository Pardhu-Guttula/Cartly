const { Sequelize } = require('sequelize');

// Epic Title: Establish Scalable Infrastructure using Next.js, Node.js, and PostgreSQL

const sequelize = new Sequelize('mydatabase', 'username', 'password', {
  host: 'localhost',
  dialect: 'postgres',
});

module.exports = sequelize;