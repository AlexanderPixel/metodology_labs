const express = require('express');
const app = express();
const port = 8080;

app.get('/', (req, res) => {
    res.send(`Received request from ${req.ip}`);
});

app.listen(port, () => {
    console.log(`Server started at http://localhost:${port}`);
});