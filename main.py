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
from libraries.solver import Solver
from libraries.scraping import Scraping
from libraries.recognition import Recognition

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
reco_cli = Recognition()
solve_cli = Solver()
templates = Jinja2Templates(directory="pages")
consumption_table = {
    "mobile": {
        "ec": "Mainly during charging and using data services.",
        "rt": [
            "Use power-saving modes.",
            "Limit background app activity.",
            "Reduce screen brightness and timeout duration.",
        ]
    },
    "computer": {
        "ec": "Desktops consume more than laptops due to larger components.",
        "rt": [
            "Use energy-efficient models (look for ENERGY STAR ratings).",
            "Enable sleep mode when inactive.",
            "Unplug chargers and peripherals when not in use.",
        ]
    },
    "microwave": {
        "ec": "Significant energy use when in operation.",
        "rt": [
            "Use for multiple items at once to maximize efficiency.",
            "Avoid opening the door frequently during cooking.",
            "Use appropriate container sizes to reduce cooking time."
        ]
    },
    "appliance": {
        "ec": "One of the largest energy consumers, especially in summer.",
        "rt": [
            "Regular maintenance, including cleaning filters.",
            "Set the thermostat higher when not home.",
            "Use fans to circulate cool air.",
        ]
    },
    "security_camera": {
        "ec": "Continuous operation contributes to energy usage.",
        "rt": [
            "Use motion-detection features to limit recording time.",
            "Switch to energy-efficient models.",
            "Schedule specific times for recording rather than continuous."
        ]
    },
    "projector": {
        "ec": "Can have a high energy draw depending on type and settings.",
        "rt": [
            "Use eco-mode settings.",
            "Turn off when not in use.",
            "Keep lenses clean to maintain efficiency."
        ]
    },
    "television": {
        "ec": "Considerable energy usage, especially larger models.",
        "rt": [
            "Use energy-saving modes.",
            "Lower brightness and contrast settings.",
            "Unplug or use smart plugs to turn off completely when not in use."
        ]
    }
}
class Image(BaseModel):  
    image_data: bytes # i patched this, json not required, use form data instead 

# app.add_middleware( # forgot when i added this
#     CORSMiddleware,
#     allow_origins = ["*"], 
#     allow_credentials = True,
#     # allow_method = ["*"],
#     allow_headers = ["*"],
# )

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

@app.get("/about", response_class = HTMLResponse)
async def about_page(request: Request):
    return templates.TemplateResponse(
        request=request, name="about.html"
    )

# no time to work on frontend to deal with response
@app.get("/404/", response_class = HTMLResponse)
async def about_page(request: Request, predicted_item: str = "Unknown"):
    return templates.TemplateResponse(
        request=request, name="notfound.html", context={"pi": predicted_item}
    )

@app.get("/electronic", response_class = HTMLResponse)
async def about_page(request: Request, electronic: str):
    i1, x1, x2, x3 = "", "", "", ""
    try:
        xyz = consumption_table[electronic]
        i1, x1, x2, x3 = xyz["ec"], xyz["rt"][0], xyz["rt"][1], xyz["rt"][2]
    except:
        print("Pass")
    return templates.TemplateResponse(
        request=request, name="electronic.html", context={"electronic": electronic, "i1": i1, "x1": x1, "x2": x2, "x3": x3},
    )

@app.get("/history", response_class = HTMLResponse)
async def history_page(request: Request):
    return templates.TemplateResponse(
        request=request, name="history.html"
    )


@app.post("/api/upload")
async def upload_image(image: UploadFile = File(...)) -> object:
    # status_code=status.HTTP_303_SEE_OTHER
    # try:
        image_byte = await image.read()
        data, is_electronic, time_taken = reco_cli.analyse_image(image_byte)
        return await response_json(
            "success",
            data = [data, is_electronic, time_taken]
        )
    # except Exception as e:
    #     return await response_json(
    #         "error",
    #         "Exception: " + str(e)
    #     )
    
@app.get("/api/solve")
async def solve_captcha() -> object:
    global reco_cli
    try:
        token = True
        while token == True: # come out the loop when it's a string / none
            id = solve_cli.create_task()
            token = solve_cli.get_task_result(id)

        reco_cli.captcha_token = token # update the captcha token (do it once a day or if blank response occurs)
        return await response_json(
            "success",
            data = token
        )
    except Exception as e:
        return await response_json(
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