from random import randint

from locust import User, TaskSet, between, task, HttpUser


class ReadWritePosts(TaskSet):
    @task(1)
    def read_posts(self):
        response = self.client.get("api/v1/posts/", name="list posts")
        print("Response status code:", response.status_code)
        print("Response content:", response.text)

    # @task(1)
    # def write_posts(self):
    #     response = self.client.post("api/v1/posts/",
    #                                 {
    #                                     "title": "title",
    #                                     "body": "body"
    #                                 },
    #                                 name="write posts")
    #     print("Response status code:", response.status_code)
    #     print("Response content:", response.text)
    #

class WebsiteUser(HttpUser):
    tasks = [ReadWritePosts]
    wait_time = between(2.0, 5.0)
