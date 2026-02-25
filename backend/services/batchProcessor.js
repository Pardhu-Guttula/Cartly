const Data = require('../models/data');

// Epic Title: Develop Data Processing Backend with Node.js

async function processBatch(batch) {
  try {
    const transaction = await Data.sequelize.transaction();

    for (const item of batch) {
      await Data.create(item, { transaction });
    }

    await transaction.commit();
    console.log(`Batch processed successfully with ${batch.length} items`);
  } catch (error) {
    console.error('Batch processing failed:', error);
    throw error;
  }
}

module.exports = {
  processBatch,
};