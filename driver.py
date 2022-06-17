from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import vars


def setup_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = vars.chrome_bin
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.delete_all_cookies()
    return driver
