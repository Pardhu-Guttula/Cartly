# Epic Title: Develop Data Processing Backend with Node.js

const express = require('express');
const bodyParser = require('body-parser');
const dataProcessorController = require('./analytics_and_reporting/controllers/data_processor_controller');

const app = express();

app.use(bodyParser.json());
app.use('/api/data_processor', dataProcessorController);

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});