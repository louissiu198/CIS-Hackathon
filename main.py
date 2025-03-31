from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from uvicorn import run
from fastapi import (
    File,
    UploadFile, 
    FastAPI,
    Request,
    Response,
    status,
)
from libraries.scraping import Scraping
from libraries.recognition import Recognition

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
reco_cli = Recognition()
templates = Jinja2Templates(directory="pages")


class Image(BaseModel): # use byte fuck
    image_data: bytes # i patch this myself, json not required, use form data instead 

# app.add_middleware( # forgot when i added this
#     CORSMiddleware,
#     allow_origins = ["*"], 
#     allow_credentials = True,
#     # allow_method = ["*"],
#     allow_headers = ["*"],
# )
            # return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER) 

async def response_json(status: str = "success", response: str = "", data: dict = {}) -> dict:
    return {
        "status": status,
        "message": response,
        "data": data
    }

@app.get("/", response_class = HTMLResponse)
async def index_page(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.get("/api/upload")
async def upload_image(image: UploadFile = File(...)) -> HTMLResponse:
    try:
        image_byte = await image.read()
        data = reco_cli.analyse_image(image_byte)
        return response_json(
            "success",
            data = data
        )

            # if user_cli.check_db_item("token", authorization): 
            #     return templates.TemplateResponse(
            #         request=request, name="lobby.html"
            #     )
    except Exception as e:
        return response_json(
            "error",
            "Exception: " + str(e)
        )

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=1234)

"""
6 underwear
1 plain socks
1 pe socks
2 blue socks (1 pe inside)
4 bottle of water

2 school trousers
bluer

tiktok_registeration
{"data":{"age_verification_type":0,"app_id":1233,"avatar_url":"https://p16-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/640b107d70a537e1fd2f37a81883459c~tplv-tiktokx-cropcenter:300:300.webp?dr=9638\u0026nonce=51015\u0026refresh_token=a78b210ba635feb678601ad73f4c47de\u0026x-expires=1741010400\u0026x-signature=hl3oJeQRMQtbTh44OF%2BLkkhrPiQ%3D\u0026idc=useast5\u0026ps=13740610\u0026shcp=9f9603f4\u0026shp=a5d48078\u0026t=4d5b0474","biz_user_info_demotion":0,"biz_user_info_string":"","cloud_token":"","cmpl_check_box_type":0,"cmpl_privacy_highlights":0,"cmpl_private_account_prompt":0,"connects":[{"platform":"facebook","platform_app_id":0,"profile_image_url":"","expired_time":1743430395,"expires_in":0,"platform_screen_name":"Cecelia Scheffler","user_id":23696102,"platform_uid":"1684400888445224","sec_platform_uid":"MS4wLjABAAAAV7F5-y325rj3txNQTV1k2MDD22C34wLD60KoMZlwQK-qfR0ENb5wnUh-p-fW5haK","modify_time":1572029279,"access_token":"","open_id":"","extra":"{}"}],"country_code":1,"device_id":0,"email":"","email_collected":false,"expired_uid_list":null,"google_odm_infos":null,"has_password":1,"id_token":"eyJhbGdvIjoiRUNEU0EzODQifQ==.
"""