from fastapi import FastAPI

from weather_api.api import get_timezone

app = FastAPI()


@app.get("/timezone/{city}")
async def timezone(city: str):
    timezone = get_timezone(city)
    return {"timezone": timezone}
