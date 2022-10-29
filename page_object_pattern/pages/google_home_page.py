from selenium.webdriver.common.by import By


class GoogleHomePage:

    def __init__(self, driver):
        self.driver = driver
        self.allow_all_cookies_xpath = "//button[@id='L2AGLb']/div"
        self.search_input_name = "q"
        self.search_button_name = "btnK"

    def allow_all_cookies(self):
        self.driver.find_element(By.XPATH, self.allow_all_cookies_xpath).click()

    def search_in_google(self, text):
        self.driver.find_element(By.NAME, self.search_input_name).send_keys(text)
        elements = self.driver.find_elements(By.NAME, self.search_button_name)
        for element in elements:
            if element.is_displayed():
                element.click()
                break
