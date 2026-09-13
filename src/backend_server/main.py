import logging

from fastapi import FastAPI
from opentelemetry import metrics, trace

from weather_api.api import get_timezone

logger = logging.getLogger("uvicorn")
tracer = trace.get_tracer(__name__)
meter = metrics.get_meter(__name__)
app = FastAPI()

item_requests_counter = meter.create_counter(
    name="requests_total",
    description="Total number of requests",
    unit="1",
)

@app.get("/timezone/{city}")
async def timezone(city: str) -> dict[str, str]:
    with tracer.start_as_current_span("get-timezone") as span:
        span.set_attribute("city", city)
        item_requests_counter.add(1, {"city": city})
        timezone = get_timezone(city)
        logger.info(f"Timezone for {city}: {timezone}")
        return {"timezone": timezone}
