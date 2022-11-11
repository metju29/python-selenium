import logging
import random

from selenium.common import NoSuchElementException

from selenium_demo.locators.locators import MyAccountPageLocators as MyAccPaLoc

logger = logging.getLogger(__name__)


class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver
        # my account page elements
        self.username_input = MyAccPaLoc.username_input
        self.password_input = MyAccPaLoc.password_input
        self.login_button = MyAccPaLoc.login_button
        self.reg_email_input = MyAccPaLoc.reg_email_input
        self.reg_password_input = MyAccPaLoc.reg_password_input
        self.register_button = MyAccPaLoc.register_button
        self.logout_link = MyAccPaLoc.logout_link
        self.addresses_link = MyAccPaLoc.addresses_link
        self.woocommerce_error_alert = MyAccPaLoc.woocommerce_error_alert
        self.woocommerce_message_alert = MyAccPaLoc.woocommerce_message_alert

    def open_page(self):
        self.driver.get("http://seleniumdemo.com/?page_id=7")

    def log_in(self, username, password):
        logger.info(f"Test for e-mail adress: {username}")
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   self.driver.find_element(*self.password_input))
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def create_account(self, email, password):
        logger.info(f"Test for e-mail adress: {email}")
        self.driver.find_element(*self.reg_email_input).send_keys(email)
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   self.driver.find_element(*self.reg_password_input))
        self.driver.find_element(*self.reg_password_input).send_keys(password)
        self.driver.find_element(*self.register_button).click()

    def get_random_email(self):
        number = str(random.randint(0, 10000))
        email = f"test{number}@szkolenie.pl"
        return email

    def is_logout_link_displayed(self):
        try:
            self.driver.find_element(*self.logout_link).is_displayed()
        except NoSuchElementException:
            return False

    def get_error_msg(self):
        return self.driver.find_element(*self.woocommerce_error_alert).text

