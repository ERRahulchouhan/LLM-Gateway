# New API

1. Copy `.env.example` to `.env`. Generate separate strong values for the database, Redis, and session secrets, and set the exact public HTTPS origin used by your TLS reverse proxy.
2. Pin `NEW_API_IMAGE` to a tested release tag or digest.
3. Start with `docker compose up -d --build`.
4. The service is available on `http://127.0.0.1:3001`; complete initial setup and configure providers/access keys before accepting traffic.

PostgreSQL, Redis, application data, and logs use named persistent volumes. Do not publish the database or Redis ports. If you change the public hostname, update `PUBLIC_ORIGIN` to match the exact external HTTPS origin.
