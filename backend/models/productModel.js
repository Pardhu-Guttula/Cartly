const { DataTypes, Model } = require('sequelize');
const sequelize = require('../services/database');

// Epic Title: Ensure Modular Architecture for Easy Integration

class Product extends Model {}

Product.init({
  id: {
    type: DataTypes.INTEGER,
    autoIncrement: true,
    primaryKey: true,
  },
  name: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  price: {
    type: DataTypes.FLOAT,
    allowNull: false,
  },
}, {
  sequelize,
  modelName: 'Product',
});

module.exports = Product;