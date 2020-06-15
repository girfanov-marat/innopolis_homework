r"""
Performance testing with Locust.

Start: 'locust -f lesson_12_hw\web_app\performance.py'
"""
from typing import Any

from locust import HttpUser, task, between

from lesson_12_hw.web_app.utilities import json_generator


class IndexLoading(HttpUser):
    """Create client."""

    wait_time = between(2, 5)

    @task
    def status_page(self: Any) -> None:
        """GET request."""
        self.client.get("/status")

    @task
    def add_page(self: Any) -> None:
        """POST request."""
        self.client.post("/add", json=json_generator())
