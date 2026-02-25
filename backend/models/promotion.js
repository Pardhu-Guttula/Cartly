const { DataTypes, Model } = require('sequelize');
const sequelize = require('../services/database');

// Epic Title: Integrate Promotion System with Order Management

class Promotion extends Model {}

Promotion.init({
  id: {
    type: DataTypes.INTEGER,
    autoIncrement: true,
    primaryKey: true,
  },
  code: {
    type: DataTypes.STRING,
    allowNull: false,
    unique: true,
  },
  description: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  discount_amount: {
    type: DataTypes.FLOAT,
    allowNull: false,
  },
  expiration_date: {
    type: DataTypes.DATE,
    allowNull: false,
  },
}, {
  sequelize,
  modelName: 'Promotion',
});

module.exports = Promotion;