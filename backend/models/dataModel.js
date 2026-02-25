const { DataTypes, Model } = require('sequelize');
const sequelize = require('../services/database');

// Epic Title: Establish Scalable Infrastructure using Next.js, Node.js, and PostgreSQL

class Data extends Model {}

Data.init({
  id: {
    type: DataTypes.INTEGER,
    autoIncrement: true,
    primaryKey: true,
  },
  value: {
    type: DataTypes.STRING,
    allowNull: false,
  },
}, {
  sequelize,
  modelName: 'Data',
});

module.exports = Data;