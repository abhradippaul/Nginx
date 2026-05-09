# Nginx Load Balancer & Monitoring Stack

This project is a comprehensive setup demonstrating Nginx as a reverse proxy and load balancer, alongside a robust monitoring and log aggregation stack using Prometheus, Grafana, and Fluentd. 

## 🚀 Features

* **Reverse Proxy & Load Balancing:** Nginx distributes incoming traffic across three Node.js backend instances (`app1`, `app2`, `app3`).
* **HTTPS/SSL Support:** Pre-configured to support secure connections with self-signed certificates or Let's Encrypt (Certbot).
* **Static File Serving:** Nginx serves static HTML content from the `html` directory.
* **Monitoring Stack:** Integrated with Prometheus for metrics collection and Grafana for powerful visualization dashboards.
* **Log Aggregation:** Fluentd is used to collect and aggregate Nginx access and error logs.
* **Containerized Environment:** Fully managed by Docker Compose for easy setup and teardown.

## 🏗️ Architecture

The architecture consists of the following Docker containers:

* **nginx:** The core reverse proxy and load balancer.
* **app1, app2, app3:** Node.js backend services serving API endpoints (`/api`, `/api/health`).
* **nginx-prometheus-exporter:** Extracts metrics from Nginx's stub status and exposes them for Prometheus.
* **prometheus:** Time-series database that scrapes metrics from the exporter.
* **grafana:** Analytics and interactive visualization web application.
* **fluentd:** Data collector for unified logging layer.

## 📋 Prerequisites

* Docker and Docker Compose installed on your system.
* OpenSSL (for generating self-signed certificates).

## 🛠️ Setup & Installation

### 1. Generate SSL Certificates
Before starting the services, generate a self-signed certificate for Nginx (or provide your own).

```bash
mkdir -p certs
openssl req -x509 -nodes -days 365 \
  -newkey rsa:2048 \
  -keyout certs/selfsigned.key \
  -out certs/selfsigned.crt
```

*(Note: The `nginx.conf` is configured to look for these certificates in `/etc/nginx/certs/`)*

### 2. Start the Stack
Bring up all the services using Docker Compose:

```bash
docker compose up --build -d
```

## 🌐 Endpoints & Services

Once the stack is running, you can access the following services:

| Service | URL | Description |
|---|---|---|
| **Web Server (HTTP)** | `http://localhost` | Redirects to HTTPS automatically. |
| **Web Server (HTTPS)** | `https://localhost` | Serves the main static website. |
| **Backend API** | `https://localhost/api` | Load balanced API endpoint hitting `app1`, `app2`, or `app3`. |
| **Backend Health** | `https://localhost/api/health` | Health check endpoint for the backend cluster. |
| **Nginx Status** | `http://localhost:8080/status` | Raw Nginx stub status (internal monitoring). |
| **Grafana** | `http://localhost:3000` | Grafana Dashboard (Default Login: `admin`/`admin`). |
| **Prometheus** | `http://localhost:9090` | Prometheus UI for querying metrics directly. |

## ⚙️ Configuration Files

* `docker-compose.yaml`: Defines all services, networks, and volumes.
* `nginx.conf`: Main Nginx configuration file containing routing, SSL, upstream definitions, and custom log formats.
* `backend/server.js`: The Node.js application logic.
* `fluentd/fluent.conf`: Configuration for log parsing and routing.
* `prometheus.yml`: Prometheus scraping configuration.

## 📝 Useful Commands

**See Nginx Version:**
```bash
docker exec -it nginx nginx -v
```

**Reload Nginx Configuration (without restarting container):**
```bash
docker exec -it nginx nginx -s reload
```

**View Response Headers:**
```bash
curl -I -k https://localhost
```

## 🔐 Using Let's Encrypt (Certbot)

If you are deploying this to a public server (e.g., Ubuntu), you can use Certbot for valid SSL certificates:

```bash
# Install certbot
sudo apt update
sudo apt install -y certbot

# Create Certificate (Standalone or Webroot)
sudo certbot certonly -d your-domain.com
```
Update `nginx.conf` to point to the `/etc/letsencrypt/live/...` paths and uncomment the relevant lines.
