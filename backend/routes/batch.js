const express = require('express');
const { processBatch } = require('../services/batchProcessor');

// Epic Title: Develop Data Processing Backend with Node.js

const router = express.Router();

router.post('/batch', async (req, res) => {
  try {
    const batch = req.body;
    await processBatch(batch);
    res.json({ success: true, message: 'Batch processed successfully' });
  } catch (error) {
    res.status(500).json({ success: false, message: 'Batch processing failed' });
  }
});

module.exports = router;