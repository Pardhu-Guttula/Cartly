# Epic Title: Establish Scalable Infrastructure using Next.js, Node.js, and PostgreSQL

const express = require('express');

const apiRoutes = (pool) => {
  const router = express.Router();

  router.get('/health', (req, res) => {
    res.status(200).json({ status: 'OK' });
  });

  router.post('/data', async (req, res) => {
    const { key, value } = req.body;
    try {
      const result = await pool.query('INSERT INTO data (key, value) VALUES ($1, $2) RETURNING *', [key, value]);
      res.status(201).json(result.rows[0]);
    } catch (err) {
      console.error(err);
      res.status(500).json({ error: 'Database error' });
    }
  });

  router.get('/data', async (req, res) => {
    try {
      const result = await pool.query('SELECT * FROM data');
      res.status(200).json(result.rows);
    } catch (err) {
      console.error(err);
      res.status(500).json({ error: 'Database error' });
    }
  });

  return router;
};

module.exports = apiRoutes;