# Helicone

Helicone self-hosting is a multi-service stack (including database, cache, storage, and application services). A single-container Dockerfile or minimal Compose file would not deploy a functional production gateway.

This folder is kept separate for its own experiments and deployment notes. Use the upstream Helicone self-hosted Docker Compose deployment and its release-matched environment template. Do not run the upstream development/test Compose file as a production deployment; verify its profiles, secrets, persistence, and version pins first.

The `Dockerfile` is intentionally a marker only (`scratch`) and does not contain or build Helicone. Use the upstream deployment artifacts to build/run the actual service.
