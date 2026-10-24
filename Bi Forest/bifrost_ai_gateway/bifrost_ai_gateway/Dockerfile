# Bifrost AI Gateway
# This project uses the official Bifrost container image from Docker Hub.
# It exposes the web UI and API on port 8080, which matches the project docs.

FROM maximhq/bifrost:latest

LABEL org.opencontainers.image.title="Bifrost AI Gateway" \
      org.opencontainers.image.description="Self-hosted AI gateway for LLM routing, governance, and observability." \
      org.opencontainers.image.source="https://github.com/maximhq/bifrost"

# Keep the default Bifrost service port accessible
EXPOSE 8080

# Optional defaults for local container runs
ENV BIFROST_PORT=8080 \
    BIFROST_HOST=0.0.0.0

# Persist Bifrost state in a mounted volume when the user specifies one.
VOLUME ["/data"]

# Intentionally leave the entrypoint and default command from the official image in place.
# This preserves the upstream Bifrost startup behavior.
