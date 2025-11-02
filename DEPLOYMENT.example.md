# Deployment Guide

## Quick Start

1. Clone the repository
2. Copy `.env.example` to `.env` and configure
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python3 web_interface.py`

## Production Deployment

### Using Systemd

1. Create service file in `/etc/systemd/system/ascii-photo-mask.service`:
```ini
[Unit]
Description=ASCII Photo Mask Web Interface
After=network.target

[Service]
Type=simple
User=YOUR_USER
WorkingDirectory=/path/to/ascii-photo-mask
Environment="PATH=/path/to/venv/bin"
ExecStart=/path/to/venv/bin/python3 web_interface.py
Restart=always

[Install]
WantedBy=multi-user.target
```

2. Enable and start:
```bash
sudo systemctl enable ascii-photo-mask
sudo systemctl start ascii-photo-mask
```

### Using Nginx Reverse Proxy

```nginx
server {
    listen 80;
    server_name your-domain.com;

    client_max_body_size 50M;

    location / {
        proxy_pass http://127.0.0.1:7860;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### SSL with Certbot

```bash
sudo certbot --nginx -d your-domain.com
```

## Environment Variables

- `SERVER_HOST` - Host to bind (default: 0.0.0.0)
- `SERVER_PORT` - Port to listen (default: 7860)
