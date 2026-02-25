const Product = require('../models/productModel');

// Epic Title: Ensure Modular Architecture for Easy Integration

async function createProduct(data) {
  return await Product.create(data);
}

async function getProductById(id) {
  return await Product.findByPk(id);
}

async function getAllProducts() {
  return await Product.findAll();
}

module.exports = {
  createProduct,
  getProductById,
  getAllProducts,
};