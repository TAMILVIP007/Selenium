from os import getenv

from dotenv import load_dotenv

load_dotenv()


class vars:
    """
    Class to store all the variables used in the program.
    """

    # UserInfo
    mail = getenv("MAIL")
    password = getenv("PASSWORD")

    # screen shot api
    api = getenv("API")

    # chrome binary
    chrome_bin = "/app/.apt/usr/bin/google-chrome"
