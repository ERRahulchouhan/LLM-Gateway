# One API

1. Copy `.env.example` to `.env`, generate a unique `SESSION_SECRET`, and set `ONE_API_IMAGE` to a verified stable release tag or digest. The upstream README warns that the `latest` image can be an alpha release.
2. Start with `docker compose up -d --build`.
3. The service is available on `http://127.0.0.1:3002`.
4. Complete the initial login and immediately replace any default administrator credentials before configuring providers or accepting traffic.

This single-instance template uses One API's local SQLite database, persisted in `one_api_data`. Use a separately managed MySQL deployment and the project's documented configuration if you need multiple One API instances. Keep the service behind a TLS reverse proxy for remote access.
