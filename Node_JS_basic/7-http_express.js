const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.set('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const db = process.argv[2];

  countStudents(db)
    .then((output) => {
      res.set('Content-Type', 'text/plain');
      res.send(`This is the list of our students\n${output}`);
    })
    .catch((err) => {
      res.set('Content-Type', 'text/plain');
      res.send(`This is the list of our students\n${err.message}`);
    });
});

app.listen(port);

module.exports = app;
