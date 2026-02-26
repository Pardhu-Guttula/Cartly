# Epic Title: Develop Data Processing Backend with Node.js

const express = require('express');
const DataProcessor = require('../services/data_processor');
const router = express.Router();

const dataProcessor = new DataProcessor();
dataProcessor.connect();

dataProcessor.on('processed', (info) => console.log('Processed:', info));
dataProcessor.on('batchProcessed', (info) => console.log('Batch Processed:', info));
dataProcessor.on('realTimeProcessed', (info) => console.log('Real-Time Processed:', info));

router.post('/process', async (req, res) => {
    try {
        await dataProcessor.processLargeDataset(req.body.query);
        res.status(200).send('Processing complete');
    } catch (error) {
        console.error(error);
        res.status(500).send('Processing failed');
    }
});

router.post('/batch_process', async (req, res) => {
    try {
        await dataProcessor.batchProcess(req.body.queries);
        res.status(200).send('Batch processing complete');
    } catch (error) {
        console.error(error);
        res.status(500).send('Batch processing failed');
    }
});

module.exports = router;