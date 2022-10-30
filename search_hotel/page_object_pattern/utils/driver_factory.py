from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:

    @staticmethod
    def get_driver(browser):
        if browser == "chrome":
            options = ChromeOptions()
            options.add_argument("--kiosk")
            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        elif browser == "firefox":
            options = FirefoxOptions()
            options.add_argument("--kiosk")
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        raise Exception("Provide valid driver name.")
