
# Some insight

```bash
export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
opentelemetry-instrument \
    --traces_exporter console \
    --metrics_exporter console \
    --logs_exporter console \
    --service_name dice-server \
    flask run -p 8080

```

```bash
export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
export OTEL_METRICS_EXPORTER=console
export OTEL_TRACES_EXPORTER=console
export OTEL_METRIC_EXPORT_INTERVAL=5000
opentelemetry-instrument \
    --logs_exporter console \
    --service_name dice-server \
    flask run -p 8080

```

```bash
 export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
opentelemetry-instrument \
    --traces_exporter console \
    --metrics_exporter console \
    --logs_exporter console \
    --service_name dice-server \
    flask --app check_with_metrics run -p 8080
```

values to check `diceroller.meter`




```bash
podman run -p 4317:4317 -v ./otel-collector-config.yaml:/etc/otel-collector-config.yaml otel/opentelemetry-collector:latest --config=/etc/otel-collector-config.yaml

# then

export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
opentelemetry-instrument --logs_exporter otlp flask --app check_with_metrics run -p 8080
```