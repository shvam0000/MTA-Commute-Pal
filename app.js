const express = require('express');
const app = express();
const cors = require('cors');
const PORT = 8080;
require('dotenv').config();
const bodyParser = require('body-parser');

app.use(express.json());
app.use(cors());
app.use(bodyParser.json());

app.get('/healthcheck', (req, res) => {
  res.status(200).json({
    message: 'API OK',
  });
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
