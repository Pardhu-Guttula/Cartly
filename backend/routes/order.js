const express = require('express');
const { Sequelize } = require('sequelize');
const Order = require('../models/order');
const Promotion = require('../models/promotion');

const router = express.Router();

// Epic Title: Integrate Promotion System with Order Management

router.post('/create', async (req, res) => {
  const { total_amount, promotion_code } = req.body;

  try {
    let discount_amount = 0.0;
    let promotion = null;

    if (promotion_code) {
      promotion = await Promotion.findOne({ where: { code: promotion_code } });
      
      if (!promotion) {
        return res.status(400).json({ message: 'Invalid promotion code' });
      }

      if (new Date(promotion.expiration_date) < new Date()) {
        return res.status(400).json({ message: 'Promotion has expired' });
      }

      discount_amount = promotion.discount_amount;
    }

    const final_amount = total_amount - discount_amount;

    const order = await Order.create({
      total_amount,
      discount_amount,
      final_amount,
      promotion_code: promotion ? promotion.code : null,
      promotion_id: promotion ? promotion.id : null,
      status: 'completed'
    });

    res.json(order);
  } catch (error) {
    console.error('Error creating order:', error);
    res.status(500).json({ message: 'Failed to create order' });
  }
});

router.put('/update/:id', async (req, res) => {
  const { id } = req.params;
  const { promotion_code } = req.body;

  try {
    const order = await Order.findByPk(id);
    
    if (!order) {
      return res.status(404).json({ message: 'Order not found' });
    }

    let discount_amount = 0.0;
    let promotion = null;

    if (promotion_code) {
      promotion = await Promotion.findOne({ where: { code: promotion_code } });
      
      if (!promotion) {
        return res.status(400).json({ message: 'Invalid promotion code' });
      }

      if (new Date(promotion.expiration_date) < new Date()) {
        return res.status(400).json({ message: 'Promotion has expired' });
      }

      discount_amount = promotion.discount_amount;
    }

    const final_amount = order.total_amount - discount_amount;

    order.discount_amount = discount_amount;
    order.final_amount = final_amount;
    order.promotion_code = promotion ? promotion.code : null;
    order.promotion_id = promotion ? promotion.id : null;

    await order.save();

    res.json(order);
  } catch (error) {
    console.error('Error updating order:', error);
    res.status(500).json({ message: 'Failed to update order' });
  }
});

module.exports = router;