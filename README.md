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

## Amazon Linux Certbot

```bash
# Install certbot
sudo dnf install certbot
sudo certbot certonly
```
