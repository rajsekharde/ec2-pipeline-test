from locust import HttpUser, task, between

class TestUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_data(self):
        self.client.get("/api/data")