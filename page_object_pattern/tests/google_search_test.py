from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pytest

from page_object_pattern.pages.google_home_page import GoogleHomePage
from page_object_pattern.pages.google_result_page import GoogleResultPage

class TestGoogleSearch:

    @pytest.fixture()
    def setup(self):
        options = Options()
        options.add_argument("--kiosk")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()

    def test_google_search(self, setup):
        self.driver.get("http://www.google.pl")
        home_page = GoogleHomePage(self.driver)
        home_page.allow_all_cookies()
        home_page.search_in_google("Selenium")
        result_page = GoogleResultPage(self.driver)
        result_page.open_first_result()
        assert self.driver.title == "Selenium"

