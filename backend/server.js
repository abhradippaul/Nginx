import http from "http";

const PORT = process.env.PORT
const SERVER_NAME = process.env.SERVER_NAME

http
  .createServer((req, res) => {

    if (req.url === "/api") {
      res.end(
        `Hello from Node.js ${SERVER_NAME} backend Server. Total running ${process.uptime()}. Timestamp ${new Date().toISOString()}`
      );
    } else if (req.url === "/api/health") {
      res.end(
        `${SERVER_NAME} server is healthy. Total running ${process.uptime()}. Timestamp ${new Date().toISOString()}`
      );
    } else {
      res.end()
    }

  })
  .listen(PORT, "0.0.0.0");
