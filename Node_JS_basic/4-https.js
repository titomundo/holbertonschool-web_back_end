const { createServer } = require('node:http');

const HOST = 'localhost';
const PORT = 1245;

const server = createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello Holberton School!');
});

server.listen(PORT, HOST);
