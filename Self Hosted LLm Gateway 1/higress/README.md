# Higress

Higress is kept in its own folder. Its all-in-one/container installation has its own component ports, setup, and production requirements; do not assume a generic single-port Compose file is a production deployment.

1. Copy `.env.example` to `.env` and pin `HIGRESS_IMAGE` to a tested release tag or digest.
2. Follow the upstream Higress Docker/all-in-one installation guide for required ports, volumes, and configuration.
3. Bind any management console to localhost or a private network, enable authentication, and put public traffic behind TLS.

The Dockerfile is an image wrapper only. Check the upstream image documentation for the correct runtime command and port mapping for your version before deploying.
