# Plano

Plano is kept in its own folder. The upstream project is an agentic proxy/data plane with configuration and deployment requirements; a plain container image alone is not a complete production setup.

Use the upstream Plano deployment instructions and release-matched manifests to configure control plane, routes, providers, observability, and secrets. Verify the official image name and version before building; the Dockerfile intentionally has no guessed default image. Configure authentication and TLS before accepting traffic.

The Dockerfile is only an image wrapper. Do not assume this folder is a standalone Compose deployment.
