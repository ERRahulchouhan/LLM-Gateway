# Apache APISIX

This is an independent, single-node, file-driven APISIX deployment. It uses the documented `data_plane` + YAML configuration mode; it does not require etcd and disables the Admin API.

## Configure and start

1. Copy `.env.example` to `.env`.
2. Replace `APISIX_GATEWAY_KEY` and `OPENAI_API_KEY` with separate strong secrets. Keep `.env` private and out of source control.
3. Pin `APISIX_IMAGE` to a tested release or immutable digest.
4. Start the gateway with `docker compose up -d --build`.
5. Check status and startup errors with `docker compose ps` and `docker compose logs -f apisix`.

The sample route forwards `GET` and `POST` requests under `/v1/` to OpenAI over HTTPS. APISIX requires clients to send the gateway key in the `apikey` header, then replaces the upstream `Authorization` header with the OpenAI provider key from the container environment. For example:

```sh
curl http://127.0.0.1:9082/v1/models \
  -H "apikey: $APISIX_GATEWAY_KEY"
```

The listener is published only on `127.0.0.1:9082`. For remote production traffic, put a maintained TLS reverse proxy or load balancer in front; configure its access controls and trusted proxy behavior. The Admin API and etcd are not exposed because neither is enabled in this standalone setup.

## Route configuration

Edit `apisix.yaml` to add routes, consumers, and upstreams. Keep the final `#END` marker: APISIX requires it to load file-driven configuration. APISIX checks the file for changes and hot-reloads valid updates. The `${{APISIX_GATEWAY_KEY}}` and `${{OPENAI_API_KEY}}` values are resolved from the APISIX container environment at runtime.

This starter has one gateway client and one OpenAI upstream, not user-level key management or high availability. Rotate credentials by changing `.env` and recreating the service. For production, also configure upstream failover, rate limits/quotas, monitoring, log retention, backups for your deployment configuration, and redundant APISIX nodes behind a load balancer as required by your service. Do not expose the Docker socket, configuration files, or secrets to untrusted users.
