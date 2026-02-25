const { DataTypes, Model } = require('sequelize');
const sequelize = require('../services/database');

// Epic Title: Develop Data Processing Backend with Node.js

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
  processed: {
    type: DataTypes.BOOLEAN,
    defaultValue: false,
  },
}, {
  sequelize,
  modelName: 'Data',
});

module.exports = Data;

### Services