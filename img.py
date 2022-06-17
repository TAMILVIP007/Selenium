import os
from random import randint

from PIL import Image, ImageEnhance
from requests import post
from config import vars

async def crop_image(browser):
    browser.save_screenshot("screenshot.png")
    im = Image.open("screenshot.png")
    width, height = im.size

    # attributes
    left = 5
    top = height / 5
    right = 164
    bottom = 1.5 * height / 4

    im1 = im.crop((left, top, right, bottom))
    im3 = ImageEnhance.Brightness(im1)

    # refractor
    factor = 0.5
    im_output = im3.enhance(factor)
    im_output.save("new.png")
    return "new.png"


async def gen_captcha(browser):
    img = await crop_image(browser)
    try:
        with open(img, "rb") as f:
            f.read()
            headers = {"X-Api-Key": vars.api}
            api_url = "https://api.api-ninjas.com/v1/imagetotext"
            files = {"image": open(img, "rb")}
            r = post(api_url, files=files, headers=headers)
            if not r.json()[0]["text"]:
                os.remove(img)
                return await rand()
            os.remove(img)
            return r.json()[0]["text"]
    except Exception:
        return rand()


async def rand():
    number = randint(222222, 9999999)
    return number
