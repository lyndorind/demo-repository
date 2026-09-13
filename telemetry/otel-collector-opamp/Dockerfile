ARG OTEL_COLLECTOR_VERSION=0.160.0

FROM otel/opentelemetry-collector-opampsupervisor:${OTEL_COLLECTOR_VERSION} AS supervisor
FROM otel/opentelemetry-collector-contrib:${OTEL_COLLECTOR_VERSION} AS collector

USER 0:0
COPY --from=supervisor --chmod=755 /usr/local/bin/opampsupervisor /opampsupervisor
ENTRYPOINT ["/opampsupervisor"]
CMD ["--config", "/etc/otel/supervisor.yaml"]
