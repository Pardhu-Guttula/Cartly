const express = require('express');
const { processRealTime } = require('../services/realTimeProcessor');

// Epic Title: Develop Data Processing Backend with Node.js

const router = express.Router();

router.post('/real-time', async (req, res) => {
  try {
    const dataStream = req.body; // Assuming data stream is sent in an array format for simplicity
    await processRealTime(dataStream);
    res.json({ success: true, message: 'Real-time processing completed successfully' });
  } catch (error) {
    res.status(500).json({ success: false, message: 'Real-time processing failed' });
  }
});

module.exports = router;