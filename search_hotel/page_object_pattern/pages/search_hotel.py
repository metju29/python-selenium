from allure_commons.types import AttachmentType

from search_hotel.page_object_pattern.locators.locators import SearchHotelLocators
from selenium.webdriver.common.by import By
import logging
import allure


class SearchHotelPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    @allure.step("Setting city name to '{1}'")
    def set_city(self, city):
        self.logger.info("Setting city {}.".format(city))
        self.driver.find_element(By.XPATH, SearchHotelLocators.searchbox_span).click()
        self.driver.find_element(By.XPATH, SearchHotelLocators.searchbox_input).send_keys(city)
        self.driver.find_element(By.XPATH, SearchHotelLocators.searchbox_result_ul).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="set_city", attachment_type=AttachmentType.PNG)

    @allure.step("Setting data range from '{1}' to {2}.")
    def set_date_range(self, day_in, day_out):
        self.logger.info("Setting check in {checkin} and {checkout} dates.".format(checkin=day_in, checkout=day_out))
        self.driver.find_element(By.XPATH, SearchHotelLocators.check_in_input).click()
        self.driver.find_elements(By.XPATH, SearchHotelLocators.day_in_td)[day_in].click()
        self.driver.find_elements(By.XPATH, SearchHotelLocators.day_out_td)[day_out].click()
        allure.attach(self.driver.get_screenshot_as_png(), name="set_date_range", attachment_type=AttachmentType.PNG)

    @allure.step("Setting travellers adults - '{1}' and childs - '{2}'.")
    def set_travellers(self, adults, childs):
        self.logger.info("Setting travellers adults - {adults} and childs - {kids}.".format(adults=adults, kids=childs))
        self.driver.find_element(By.XPATH, SearchHotelLocators.travellers_input).click()
        self.driver.find_element(By.XPATH, SearchHotelLocators.adult_input).clear()
        self.driver.find_element(By.XPATH, SearchHotelLocators.adult_input).send_keys(adults)
        self.driver.find_element(By.XPATH, SearchHotelLocators.child_input).clear()
        self.driver.find_element(By.XPATH, SearchHotelLocators.child_input).send_keys(childs)
        allure.attach(self.driver.get_screenshot_as_png(), name="set_travellers", attachment_type=AttachmentType.PNG)

    def perform_serach(self):
        self.logger.info("Performing search.")
        self.driver.find_element(By.XPATH, SearchHotelLocators.search_button).click()


