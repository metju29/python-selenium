from selenium.webdriver.common.by import By


class GoogleResultPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_results_xpath = "//div[@class='kvH3mc BToiNc UK95Uc']//h3"

    def open_first_result(self):
        self.driver.find_elements(By.XPATH, self.search_results_xpath)[0].click()