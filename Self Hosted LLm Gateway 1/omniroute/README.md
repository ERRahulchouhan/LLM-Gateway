# OmniRoute

This folder runs OmniRoute independently and stores application data in the `omniroute_data` volume.

1. Copy `.env.example` to `.env` and pin the container image to a tested release.
2. Start with `docker compose up -d --build`.
3. The upstream Docker instructions use port 20128; this stack binds it to localhost.
4. Complete the first-run setup, configure provider credentials, and secure the service before use.

Follow upstream requirements for memory limits, image updates, and backups. Keep the service behind a TLS reverse proxy for remote access.
