# agentgateway

agentgateway is an independent standalone proxy for AI agents and MCP traffic. It requires an explicit listener/route configuration; do not expose an unconfigured proxy.

1. Copy `.env.example` to `.env` and pin `AGENTGATEWAY_IMAGE` to a tested release tag or digest.
2. Follow the official standalone deployment documentation to create and validate a configuration file.
3. Configure authentication, upstream allowlists, TLS, and authorization policies before exposing listeners.

The Dockerfile wraps the upstream image. This folder intentionally does not guess a configuration schema or start an open proxy. Use the upstream configuration reference to supply the version-compatible standalone config.
