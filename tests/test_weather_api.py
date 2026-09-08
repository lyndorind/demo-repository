import pytest
from weather_api.api import get_timezone

def test_get_timezone():
    timezone = get_timezone("Kyiv")
    assert timezone == "Europe/Kyiv"
