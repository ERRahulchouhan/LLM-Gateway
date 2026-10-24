# vLLM Semantic Router

This is an independent folder for the vLLM Semantic Router decision layer. It is typically deployed alongside model-serving infrastructure and a router configuration; the router image alone is not a complete production LLM platform.

1. Verify the correct image name and version from upstream's release instructions; the Dockerfile intentionally has no guessed default image.
2. Follow upstream deployment instructions for the matching version, including its router configuration, model backends, and dependencies.
3. Configure TLS, authentication, and model access policies before accepting traffic.

The Dockerfile is an image wrapper, not a complete deployment manifest. Do not start it without the release-matched configuration and dependencies.
