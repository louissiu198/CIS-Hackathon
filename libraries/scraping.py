from urllib.parse import quote
from httpx import Client
from uuid import uuid4

electronics = [ # things to scrape
    # "security_cameras",
    # "television",
    # "mobile_phone",
    # "ipad",
    "computer",
    # "telephone",
    "lights",
    "air_condition",
    "microwave",
    "projectors"
]

class Scraping:
    def __init__(self):
        self.client = Client(http2 = True, verify = False) # add proxy to prevent ip ratelimit
        self.endpoint = "https://www.freepik.com/"
    
    def search_images(self, page: int = 1, content: str = "pass on") -> Client:
        return self.client.get(
            f"https://www.freepik.com/api/regular/search?locale=en&page={page}&term=" + quote(content),
            headers = {
                "accept":"*/*",
                "accept-encoding":"gzip, deflate, br, zstd",
                "accept-language":"en-GB,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh;q=0.6",
                "dnt": "1", # cookie might expire / recapture
                "cookie": "_ga=GA1.1.674242191.1729259158; _cs_c=0; OptanonAlertBoxClosed=2024-10-18T13:47:20.156Z; ab.storage.userId.35bcbbc0-d0b5-4e6c-9926-dfe1d0cd06ab=g%3A138618992%7Ce%3Aundefined%7Cc%3A1729259313404%7Cl%3A1729259313413; ab.storage.deviceId.35bcbbc0-d0b5-4e6c-9926-dfe1d0cd06ab=g%3A91fd6fd9-2cda-6fe4-b4d5-46137ecfc3cd%7Ce%3Aundefined%7Cc%3A1729259313421%7Cl%3A1729259313421; ab.storage.sessionId.35bcbbc0-d0b5-4e6c-9926-dfe1d0cd06ab=g%3A7d3b8bec-596c-5412-326f-422c4f760e48%7Ce%3A1729295313432%7Cc%3A1729259313409%7Cl%3A1729259313432; _hjSessionUser_1331604=eyJpZCI6IjgxNGVjMzM0LWEyNTgtNTg1Yy05ZWU5LWQ2MzNiMGE2MDQ5YSIsImNyZWF0ZWQiOjE3MjkyNTkzMTM5ODgsImV4aXN0aW5nIjpmYWxzZX0=; _ga_Q29FZ8F7H4=GS1.1.1729261398.2.0.1729261398.0.0.0; ph_phc_Rc6y1yvZwwwR09Pl9NtKBo5gzpxr1Ei4Bdbg3kC1Ihz_posthog=%7B%22distinct_id%22%3A%2214778686%22%2C%22%24sesid%22%3A%5B1735203134448%2C%220194022a-2ce8-7379-9dbc-9c131246fb64%22%2C1735203106024%5D%2C%22%24epp%22%3Atrue%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22https%3A%2F%2Fwww.freepik.com%2Fai%2Fvideo-generator%22%2C%22u%22%3A%22https%3A%2F%2Fwww.freepik.com%2Fpikaso%2Fai-video-generator%23from_element%3Dlanding_video_generator%22%7D%7D; _gcl_au=1.1.493636758.1743387893; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Mar+31+2025+10%3A30%3A36+GMT%2B0800+(Hong+Kong+Standard+Time)&version=202503.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=fcdaf456-b692-4f10-ba1f-fcf84c7c6dd2&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1&intType=1&geolocation=HK%3B&AwaitingReconsent=false; ak_bmsc=A1AF642C887097DE4BA3E42A3D624858~000000000000000000000000000000~YAAQLCLKF7h/BtGVAQAAkzB/6hubD4K8r+b4niQ0LvZkg6NRVBX9In287L7gDSIf4NvwBNozTs2XsbJ2gayIBO6fNngfGfGJcfElGGEWkkNRLQGSqT6HhbvrQsa/VNsuUWpFE6UgBRGu8Y5enudZ7vUzALYnV4qlIEeIbrM90hiGX1FvrKXQjfIOFAtm9wDePyjP6Y3gBFRk6psHKJ7RImWv4Zigr7RE8goTeM94tI1alyv2/0J+S6WKAJAQrfnt1/7VA03XCbNtU12T5xQkZq0meueGrVG5unDhLW0C96fLhES0EzYgL7UyTKe0J9BKuGgUnAtqEQP+TimTdFPcRmorBCgWFcAS8nWoaiV5C1rX9AYRa4rVQKsHmspB7uCxLJ0=; _ga_QWX66025LC=GS1.1.1743395958.4.0.1743395958.60.0.0",
                "if-none-match": 'W/"ysya4y8918t4v"',
                "priority": "u=1, i",
                "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
            }
        )
    
    def scrape_images(self, content: str = "Cctv Camera") -> list:
        t = []
        r = self.search_images(1, content)
        if "pagination" not in r.text: 
            return []
        amountPage = r.json()["pagination"]["lastPage"]

        for x in range(1, 10 if amountPage > 50 else 5):
            r = self.search_images(x, content).json()
            for item in r["items"]:
                t.append(item["preview"]["url"])
        return t

    def load_images(self, model_name: str, url: str) -> None:
        try:
            y = self.client.get(url).content
            with open(f'./models/{model_name}/{str(uuid4())}.jpg', 'wb') as f:
                f.write(y)
        except Exception as e:
            print(e)
            pass

if __name__ == "__main__":
    scraper = Scraping()
    for device in electronics:
        image_list = scraper.scrape_images(device)
        for image in image_list:
            scraper.load_images(device, image)