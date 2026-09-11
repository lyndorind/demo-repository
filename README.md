# Demo Repository

This is a demo repository.

Add OTeL requirements (once):

```bash
uv run opentelemetry-bootstrap -a requirements | uv add --group otlp --requirement -
```

Launch the application:

```bash
uv run python -m backend_server
```
