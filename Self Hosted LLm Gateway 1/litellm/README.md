# LiteLLM

1. Copy `.env.example` to `.env`, generate unique secrets, and set `OPENAI_API_KEY`.
2. Pin `LITELLM_IMAGE` to a tested release tag or digest.
3. Start with `docker compose up -d --build`.
4. The proxy is available on `http://127.0.0.1:4000`; use the configured `LITELLM_MASTER_KEY` for API requests.

The starter config routes `gpt-4o-mini` to OpenAI. Change `config.yaml` and add the corresponding provider credentials to `.env` for your own models. PostgreSQL data is kept in the `litellm_postgres_data` volume.

Keep the service behind a TLS reverse proxy for remote use. The bundled notebook only checks the models endpoint; it does not send a billable completion.
