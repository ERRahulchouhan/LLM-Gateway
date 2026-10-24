# Envoy AI Gateway

This project is Kubernetes-first: a production deployment requires its supported Envoy Gateway/Kubernetes components and upstream manifests. A single Docker container is not a complete Envoy AI Gateway installation.

The `Dockerfile` requires an explicit image build argument; it intentionally does not guess an upstream image name. Verify the official image name and supported release for your chosen deployment before building it; do not assume `docker compose up` will create a working gateway. Use the upstream Envoy AI Gateway documentation and release manifests for the actual server deployment.

The notebook is a client-side smoke-test template. Set `GATEWAY_BASE_URL` to a deployed gateway endpoint and configure the auth header as required by your route.
