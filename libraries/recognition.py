from tls_client import Session # google blocked non-tls 
from base64 import b64encode
from httpx import get # fastest client
from time import time

class Recognition:
    def __init__(self, client: Session = Session("chrome_131")): # don't change tls
        self.client = client 
        self.captcha_token = "03AFcWeA7InPpInzinwABe65Pykga8Mg4T9GvLTXPcDrlc0eP1eNgI1gEB60Lgj4MArHFlely5VtPTyl80bJHP_Ps4b2mjC00iD21K9hG7HMn7RNntzJsNLTBVfzT97LwPA3rTMiit1CbvuD4n4kJKzRGy0s-OZWy_cHmiKJjMU1YLKRKBRjbIegd68hzYdkLrIm79ViG6MlVA-SJRVnM3LrCq4tlARrbbo-1XWZl_-N0gOyUeEoY3ixxd6Ysp8j-tPkPvZA9XAWf6DKSPxmB8vJjlB9YesaGKlapGnZfkiIhbCMvLJRfmWWkoMaurh3-9tv1F0K5vxG2bNaRvnD5NWcanw-9_U5vs-pvBNqMFvZU2ZI9TJ5jaAOWUCcNUPFEaWJBUCgmBNaX4cadLknlJ37G4pQQKQubAXyvXxd2A-dRVl7l5UgXsOAe2gLwA8QjzEe1WxDuejf5w93GPNPoJmqUN7_aCHenoDdtDGj51NcNnGt3gys5FzkIzUbHtxI07-a8p_lI5TazUw4KWSwbUsK5cMI6DHGdLe-y9cIM4VhVL-s5_V1RrXl4grpLVeGEcQkRqJZ8x0YsijneZdwFjiYQGZERg86jfK1Bu5bDqRPz31L7Y1xmYTr8nO4536I77_Hmh5P7rajYR_UXqwxeg2cwPsxwt3H9wgqFAYAjJ3oBo9POcnCvTPz4_5JS2b-YdNQrHHPD6EYynQ-r10Fq36cvvxXQw9ba_nN71TDB094i7kcV08HOMDkx3cxPf_ufqiRYTB2DwuXjvQSp4NV9lE7u3JIdiNpIovI9Pd2LWJ9KTR7fqtd1jUH2ODgoMKwwGjAwcfDCDKHUAUtEY-3ATs0w6rQVTLZj-3f4sg5DLqQQMxluka9Gnvazlc5cDb_Fx4vXFSIl8LEc0lOW6g8Q5crsX9tpLAxWo64od_ZycUsFTMTtma_pWc7XL3j_44bhCgGWtZQkkAG_dCU5oa4RjlKJwIdEyIfh-ZQ"
    
    def analyse_image(self, image_byte: bytes) -> object | int: # list idk
        start_time = time()
        encoded_bytes = b64encode(image_byte).decode("utf-8")
        
        payload = {
            'requests': [{
                "image": {"content": encoded_bytes},
                "features": [
                    {'maxResults': 7,'type': 'LABEL_DETECTION'},
                    {'maxResults': 7,'type': 'LOGO_DETECTION'},
                    {'maxResults': 7,'type': 'OBJECT_LOCALIZATION'},
                    {'maxResults': 7,'type': 'LANDMARK_DETECTION'},
                    {'maxResults': 7,'type': 'DOCUMENT_TEXT_DETECTION'},
                    {'maxResults': 7,'type': 'LOGO_DETECTION'}
                ]
            }]
        }

        response = self.client.post(
            'https://cxl-services.appspot.com/proxy?url=https%3A%2F%2Fvision.googleapis.com%2Fv1%2Fimages%3Aannotate&token=' + self.captcha_token, # recaptchaV2 / intercept and update / capsolver
            json = payload,
            headers = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br, zstd',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh;q=0.6',
                'content-type': 'text/plain;charset=UTF-8',
                'dnt': '1',
                'origin': 'https://www.gstatic.com',
                'priority': 'u=1, i',
                'referer': 'https://www.gstatic.com/',
                'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
            }
        )
        # print(response.text) # Debug
        if "response" not in response.text:
            return "No response! Please refresh the IP/captcha"

        r = response.json()["responses"]
        return_dict = {}
        label_annotation, object_annotation = [], []
        if "labelAnnotations" in response.text: # some photos doesnt return object annotation
            label_annotation = r[0]["labelAnnotations"]
            if len(label_annotation) != 0:
                return_dict["label"] = {
                    "item_name": label_annotation[0]["description"], 
                    "item_score": round(label_annotation[0]["score"] * 100, 2)
                }
        if "localizedObjectAnnotations" in response.text:
            object_annotation = r[0]["localizedObjectAnnotations"]
            if len(object_annotation) != 0:
                return_dict["label"] = {
                    "item_name": object_annotation[0]["name"], 
                    "item_score": round(object_annotation[0]["score"] * 100, 2)
                }

        # if len(label_annotation) == 0 or len(object_annotation) == 0:
        #     return "An error has occured"

        return return_dict, round(time() - start_time, 2)

if __name__ == "__main__":
    test_image = get("https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/MA7F4?wid=2000&hei=2000&fmt=jpeg&qlt=90&.v=1723162550519").content
    anaylsed_data, _ = Recognition().analyse_image(test_image)
    print(anaylsed_data)
