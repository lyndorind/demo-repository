import uvicorn
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter
from opentelemetry.sdk._logs import LoggerProvider
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor

provider = LoggerProvider()
processor = BatchLogRecordProcessor(OTLPLogExporter())
provider.add_log_record_processor(processor)

log_config = uvicorn.config.LOGGING_CONFIG.copy()
log_config["handlers"]["otel"] = {
    "()": "opentelemetry.sdk._logs.LoggingHandler",
    "level": "INFO",
    "logger_provider": provider,
}
log_config["loggers"]["uvicorn.access"]["handlers"].append("otel")
log_config["loggers"]["uvicorn.error"].setdefault("handlers", []).append("otel")
log_config["loggers"]["uvicorn"]["handlers"].append("otel")
