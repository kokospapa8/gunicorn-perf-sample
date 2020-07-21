from random import randint

from locust import User, TaskSet, between, task, HttpUser


class ReadPosts(TaskSet):
    @task(1)
    def read_posts(self):
        response = self.client.get("api/v1/posts/", name="list posts")
        print("Response status code:", response.status_code)
        print("Response content:", response.text)

        # csrftoken = response.cookies["csrftoken"]
        # self.client.post(
        #     "/polls/1/vote/",
        #     {"choice": str(randint(1, 4))},
        #     headers={"X-CSRFToken": csrftoken},
        # )

class WebsiteUser(HttpUser):
    tasks = [ReadPosts]
    wait_time = between(1.0, 2.0)
