const express = require('express');
const batchRouter = require('./batch');
const realTimeRouter = require('./real-time');

// Epic Title: Develop Data Processing Backend with Node.js

const router = express.Router();

router.use('/batch', batchRouter);
router.use('/real-time', realTimeRouter);

module.exports = router;

### Main Application