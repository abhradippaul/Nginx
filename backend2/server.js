import http from "http";

http
  .createServer((req, res) => {
    res.end("Hello from Node.js backend Server 2!");
  })
  .listen(3002, "0.0.0.0");
