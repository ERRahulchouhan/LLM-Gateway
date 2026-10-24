# Kong Gateway

This folder runs a standalone, DB-less Kong Gateway. It is an independent stack and starts with an empty declarative route configuration.

1. Copy `.env.example` to `.env` and pin `KONG_IMAGE` to a tested release tag or digest.
2. Review the management API exposure in `docker-compose.yml`. It is bound to localhost for local administration; do not expose port 8001 publicly.
3. Add routes, upstreams, authentication, and rate limits to `kong.yml`.
4. Start with `docker compose up -d --build`.

The proxy is available on `http://127.0.0.1:8000`. Kong's AI proxy capabilities and plugins may be edition- or license-dependent; verify your chosen feature set against current Kong licensing and documentation before production use. Place a TLS reverse proxy in front of public traffic.
