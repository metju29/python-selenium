from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pytest

class BaseTest:

    @pytest.fixture()
    def setup(self):
        options = Options()
        options.add_argument("--kiosk")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()
