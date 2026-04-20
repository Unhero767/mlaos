from locust import HttpUser, task, between

class MagisterialSwarm(HttpUser):
    wait_time = between(0.1, 0.5)

    @task
    def stress_test_rollback(self):
        # The full ritual lifecycle
        self.client.post("/start_transaction")
        self.client.post("/insert_partial_data")
        self.client.post("/simulate_failure")
        self.client.post("/rollback")

    @task(1)
    def check_health(self):
        # The Silicon Eye audit
        self.client.get("/health")
