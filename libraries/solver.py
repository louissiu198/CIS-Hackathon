from httpx import Client 
from time import sleep

class Solver:
    def __init__(self, client: Client = Client(http2 = True, timeout = 10)):
        self.client = client
        self.headers = {
            "content-type": "application/json"
        }
        self.endpoint = "https://api.capsolver.com/"
    
    def create_task(self) -> str:
        payload = {
            "clientKey": self.key,
            "appId": "",
            "task": {
                "type": "ReCaptchaV2TaskProxyLess",
                "websiteURL": "https://cloud.google.com/vision#demo",
                "websiteKey": "6LdBnhQUAAAAAMkYSqdAnkafemcA6JtM1N3hlgiL",
            },
            "isInvisible": False,
        }

        return self.client.post(
            self.endpoint + "createTask",
            json = payload,
            headers = self.headers
        ).json()["taskId"]

    def get_task_result(self, taskId: str) -> str:
        payload = {
            "clientKey": self.key,
            "taskId": taskId
        }
        for x in range(30):
            try:
                response = self.client.post(
                    self.endpoint + "getTaskResult",
                    json = payload,
                    headers = self.headers
                )
                print(response.text)
                if "ready" in response.text:
                    return response.json()["solution"]["gRecaptchaResponse"]
                elif "Failed to solve" in response.text:
                    return True
                sleep(1)
            except:
                continue

if __name__ == "__main__":
    solver = Solver()
    while True:
        id = solver.create_task()
        print(id)
        token = solver.get_task_result(id)
        if token != True:
            break
    print(token)
