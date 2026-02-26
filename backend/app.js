# Epic Title: Establish Scalable Infrastructure using Next.js, Node.js, and PostgreSQL

const express = require('express');
const bodyParser = require('body-parser');
const { Pool } = require('pg');
const apiRoutes = require('./routes/api');

const app = express();
const port = 4000;

const pool = new Pool({
  user: 'user',
  host: 'localhost',
  database: 'marketplace',
  password: 'password',
  port: 5432,
});

app.use(bodyParser.json());

app.use('/api', apiRoutes(pool));

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});