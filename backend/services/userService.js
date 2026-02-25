const User = require('../models/userModel');

// Epic Title: Ensure Modular Architecture for Easy Integration

async function createUser(data) {
  return await User.create(data);
}

async function getUserById(id) {
  return await User.findByPk(id);
}

async function getAllUsers() {
  return await User.findAll();
}

module.exports = {
  createUser,
  getUserById,
  getAllUsers,
};