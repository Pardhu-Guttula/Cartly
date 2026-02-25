const { DataTypes, Model } = require('sequelize');
const sequelize = require('../services/database');
const Promotion = require('./promotion');

// Epic Title: Integrate Promotion System with Order Management

class Order extends Model {}

Order.init({
  id: {
    type: DataTypes.INTEGER,
    autoIncrement: true,
    primaryKey: true,
  },
  total_amount: {
    type: DataTypes.FLOAT,
    allowNull: false,
  },
  discount_amount: {
    type: DataTypes.FLOAT,
    defaultValue: 0.0,
  },
  final_amount: {
    type: DataTypes.FLOAT,
    allowNull: false,
  },
  promotion_code: {
    type: DataTypes.STRING,
    allowNull: true,
  },
  status: {
    type: DataTypes.STRING,
    defaultValue: 'pending',
  },
}, {
  sequelize,
  modelName: 'Order',
});

Order.belongsTo(Promotion, { foreignKey: 'promotion_id' });

module.exports = Order;