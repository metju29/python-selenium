from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    # def __set__(self, obj, value):
    #     """Sets the text to the value supplied"""
    #     driver = obj.driver
    #     locator = value[0]
    #     text = value[1]
    #     WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.NAME, locator))
    #     driver.find_element(By.NAME, locator).clear()
    #     driver.find_element(By.NAME, locator).send_keys(text)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""

        driver = obj.driver
        WebDriverWait(driver, 100).until(lambda driver: driver.find_element(By.NAME, 'q'))
        driver.find_element(By.NAME, 'q').clear()
        driver.find_element(By.NAME, 'q').send_keys('pycon')
        return driver.find_element(By.NAME, 'q').is_displayed()
