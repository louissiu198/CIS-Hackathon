from tls_client import Session # google blocked non-tls 
from base64 import b64encode
from httpx import get # fastest client

class Recognition:
    def __init__(self, client: Session = Session("chrome_131")): # don't change tls
        self.client = client 
        self.captcha_token = "03AFcWeA41EELIwMcrLP8erdEIwYkkCIcBeq2HeC1wEIg5vSHPAgsW56Q1yK76hiuwVxcP01IvRhX1Pz61IyucxScKZ1sgtFHv_7DS-7Vd-D82OL2JP98ff7HIUzmUQNOYtItcj9uH9PkH24YQUKMyp4M0-27tWdb_meOwx8Y7YUtpBXP-PXuuI0YpLYs4S-7xbwpLEJM8KYxxC92aPavTfYwcZJHB3gFw6nYC3YkauZdQvFOnbNr0FtKH0GkA1yUoKmpW3sSdMjveue8NvRXWsJ1dXPxSy5oobSQI5jBuMv-N17edGnmI-E7j_SWkWgwOccxTQv_9OCAMK2Ciwnl1wVGSHkUEuuJkaW-_5rulnq2XxATjRPhiEPzR9TtsKNBuHUOOrhxDwVJXhzRpVw2o8_Cy6puatNdRP1BWsR3A137HI8PoEP3ljV8FYkBDhyAbDB0ihV1ZV5OHvi2CPY2QmA4LxGcpTkvy0BCKrAysfV3bvIgs6tN-wQ32XhHSLCVfkcqX7_u_1-sh7knOXFsR7XxEVojRu05lMfqme-AydceJw9Nr6k4VQec96nbBe6uXBWlKLTKER1dpGx13fOm2V53HNULbqDUUuriQiPEEf3ubngrKt9y58jdzMuwOYgifXkjkOsxqhk3gbf0M9RFBx2DGGGp5bEiZQFO6ofsFZ_2aUfGBb61y4PdohfYaxdw0Ywfi7tOl8durdZ6dmhzbDSEV1jz6R3y0dl24C97iU5o-CLnoDJ9Kp32MO0-aSSXX7nKqnRlxUtSZgjVEddzbtDkvXD5VS78y9d5RfDLou_MHEWVVMzJ4SKx16iqbTKCL1012gbwsVvJQDPsCIJmnD1nYDJvjrcQlIxKbGEQHu7QN4jP4-6QI3Ckw0HJ2ESWOFDMqW6LkJp4Twwm9EkB2I_uvpu5lbphkRWzKURXvhyVUKrrRzW6iwlDlKAZI1MXuriUftcH00o9vv2VEdKPN2jJUjzKdktw2EOYAnUk7I6Vxtawtn_hZDl4bnbYsnpKssDI6Dx4uYE0U"
    
    def analyse_image(self, image_byte: bytes) -> object: # list idk
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
        
        if "response" not in response.text:
            return "No response! Please refresh the IP/captcha"

        r = response.json()["responses"]
        label_annotation = r[0]["labelAnnotations"]
        object_annotation = r[0]["localizedObjectAnnotations"]

        if len(label_annotation) == 0 or len(object_annotation) == 0:
            return "An error has occured"

        return {
            "label": {
                "item_name": label_annotation[0]["description"], 
                "item_score": round(label_annotation[0]["score"] * 100, 2)
            },
            "object": {
                "item_name": object_annotation[0]["name"], 
                "item_score": round(object_annotation[0]["score"] * 100, 2)
            }
        }

if __name__ == "__main__":
    test_image = get("https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/MA7F4?wid=2000&hei=2000&fmt=jpeg&qlt=90&.v=1723162550519").content
    anaylsed_data = Recognition().analyse_image(test_image)
    print(anaylsed_data)