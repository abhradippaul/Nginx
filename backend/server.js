import http from "http";

const PORT = process.env.PORT
const SERVER_NAME = process.env.SERVER_NAME

http
  .createServer((req, res) => {
    res.end(`Hello from Node.js backend Server ${SERVER_NAME}!`);
  })
  .listen(PORT, "0.0.0.0");
