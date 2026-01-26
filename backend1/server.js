import http from "http";

http
  .createServer((req, res) => {
    res.end("Hello from Node.js backend Server 1!");
  })
  .listen(3001, "0.0.0.0");
