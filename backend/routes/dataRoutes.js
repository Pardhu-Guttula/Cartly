const express = require('express');
const Data = require('../models/dataModel');

// Epic Title: Establish Scalable Infrastructure using Next.js, Node.js, and PostgreSQL

const router = express.Router();

router.get('/data', async (req, res) => {
  try {
    const data = await Data.findAll();
    res.json(data);
  } catch (error) {
    console.error('Failed to fetch data:', error);
    res.status(500).json({ message: 'Failed to fetch data' });
  }
});

router.post('/data', async (req, res) => {
  try {
    const { value } = req.body;
    const newData = await Data.create({ value });
    res.status(201).json(newData);
  } catch (error) {
    console.error('Failed to create data:', error);
    res.status(500).json({ message: 'Failed to create data' });
  }
});

module.exports = router;