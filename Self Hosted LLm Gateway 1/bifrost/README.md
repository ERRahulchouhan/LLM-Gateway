# Bifrost

1. Copy `.env.example` to `.env` and pin `BIFROST_IMAGE` to a tested release tag or digest.
2. Start with `docker compose up -d --build`.
3. The built-in interface is available on `http://127.0.0.1:8080`.
4. Configure provider credentials and gateway authentication in Bifrost before routing requests.

The stack persists Bifrost's `/app/data` in the `bifrost_data` volume. Keep the service behind a TLS reverse proxy for remote access.
