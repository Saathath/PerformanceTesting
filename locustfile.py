from locust import HttpUser, task, between, tag
import urllib3
import random
from utils.student_helper import generate_random_student

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class WebsiteUser(HttpUser):
    host = "https://localhost:7229"
    wait_time = between(1, 3)

    def on_start(self):
        self.student_ids = []
        s = generate_random_student()
        self.client.post("/api/Student", json=s, verify=False)
        self.student_ids.append(s["id"])

    @task
    @tag("get_all")
    def get_all_students(self):
        self.client.get("/api/Student", verify=False)

    @task
    @tag("get_by_id")
    def get_student_by_id(self):
        sid = random.choice(self.student_ids)
        self.client.get(f"/api/Student/{sid}", verify=False)

    @task
    @tag("create")
    def create_student(self):
        s = generate_random_student()
        self.client.post("/api/Student", json=s, verify=False)
        self.student_ids.append(s["id"])

    @task
    @tag("update")
    def update_student(self):
        sid = random.choice(self.student_ids)
        s = generate_random_student()
        s["id"] = sid
        self.client.put(f"/api/Student/{sid}", json=s, verify=False)

    @task
    @tag("delete")
    def delete_student(self):
        if not self.student_ids:
            return
        sid = self.student_ids.pop()
        self.client.delete(f"/api/Student/{sid}", verify=False)
