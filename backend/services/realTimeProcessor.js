const Data = require('../models/data');

// Epic Title: Develop Data Processing Backend with Node.js

async function processRealTime(dataStream) {
  try {
    for await (const item of dataStream) {
      await Data.create(item);
    }
    console.log('Real-time processing completed successfully');
  } catch (error) {
    console.error('Real-time processing failed:', error);
    throw error;
  }
}

module.exports = {
  processRealTime,
};

### Routes