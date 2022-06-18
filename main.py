import asyncio
from warnings import filterwarnings

from selenium.webdriver.common.by import By
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import utc
from driver import setup_browser
from img import gen_captcha
from config import vars

filterwarnings("ignore")


async def main():
    browser = setup_browser()
    browser.get("https://digirms.com/dmslite/login.php?SA=27840&Login&F=4974106")
    mail = browser.find_element(By.NAME, "Email")
    password = browser.find_element(By.NAME, "Password")
    mail.send_keys(vars.mail)
    password.send_keys(vars.password)
    browser.find_element(By.NAME, "Login").click()
    await asyncio.sleep(5)
    browser.find_element(By.LINK_TEXT, "Captcha Entry").click()
    await asyncio.sleep(35)
    while True:
        try:
            button = browser.find_element(By.XPATH, "//input[@type='text']")
            text = await gen_captcha(browser)
            button.send_keys(text)
            browser.find_element(By.XPATH, "//button[@ng-if='countDown<=0']").click()
            print("Captcha: " + text + " sent")
            await asyncio.sleep(30)
        except BaseException:
            pass


print("Starting...")
loop = asyncio.get_event_loop()
scheduler = AsyncIOScheduler()
scheduler.add_job(main(), 'interval', seconds=900)
scheduler.start()
loop.run_until_complete(main())
