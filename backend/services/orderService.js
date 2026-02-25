const Order = require('../models/orderModel');

// Epic Title: Ensure Modular Architecture for Easy Integration

async function createOrder(data) {
  return await Order.create(data);
}

async function getOrderById(id) {
  return await Order.findByPk(id);
}

async function getAllOrders() {
  return await Order.findAll();
}

module.exports = {
  createOrder,
  getOrderById,
  getAllOrders,
};

### Routes