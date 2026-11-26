FROM python:3.11-slim

LABEL org.opencontainers.image.source="https://github.com/deepakshe/b2b-mcp-apify-scrapers-hub"
LABEL org.opencontainers.image.licenses="MIT"

WORKDIR /app
COPY server.py README.md LICENSE ./

CMD ["python", "server.py"]
