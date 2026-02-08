# Nginx Learning

```bash
# See Nginx version
nginx -v

# Reload Nginx
nginx -s reload

# View response header
curl -I localhost
```

```bash
# Request self signed certificate
openssl req -x509 -nodes -days 365 \
  -newkey rsa:2048 \
  -keyout selfsigned.key \
  -out selfsigned.crt
```

```bash
# Build Docker Compose
docker compose up --build -d
```

## Ubuntu Certbot

```bash
# Install certbot
sudo apt install -y certbot

# Create Certificate
sudo certbot certonly -d abhradip-nginx.duckdns.org
```
