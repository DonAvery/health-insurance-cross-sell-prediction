import numpy as np
from locust import task
from locust import between
from locust import HttpUser

sample = {
  "id": 61311,
  "gender": "male",
  "age": 68,
  "driving_license": 1,
  "region_code": 28.0,
  "previously_insured": 1,
  "vehicle_age": "1-2 year",
  "vehicle_damage": "no",
  "annual_premium": 32788.0,
  "policy_sales_channel": 26.0,
  "vintage": 31
}

class CustMarkTestUser(HttpUser):
    """
    Usage:
        Start locust load testing client with:
            locust -H http://localhost:3000
        Open browser at http://0.0.0.0:8089, adjust desired number of users and spawn
        rate for the load test from the Web UI and start swarming.
    """

    @task
    def classify(self):
        self.client.post("/classify", json=sample)

    wait_time = between(0.01, 2)

	
