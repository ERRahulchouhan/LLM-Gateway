# Portkey Gateway

This folder deploys only the Portkey Gateway. It is separate from every other gateway folder.

1. Copy `.env.example` to `.env` and pin `PORTKEY_IMAGE` to a tested release tag or digest.
2. Start with `docker compose up -d --build`.
3. The gateway listens on `http://127.0.0.1:8788` (container port 8787).
4. Configure authentication, provider integrations, and guardrails according to the upstream release documentation before accepting traffic.

The gateway configuration example at the upstream repository uses an admin token and provider credentials. Do not mount or commit credentials until they have been replaced with secrets managed by your deployment platform. This starter does not expose an admin token or configure provider integrations.
