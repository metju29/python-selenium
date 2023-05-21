import random

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

import logging

from selenium_demo.pages.billing_address_page import BillingAddressPage
from selenium_demo.pages.my_account_page import MyAccountPage

logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("setup")
class TestUpdateBillingAddress:

    def test_update_billing_address(self):
        my_account_page = MyAccountPage(self.driver)

        email = my_account_page.get_random_email()
        password = "TestTestTest12345#"

        my_account_page.open_page()
        my_account_page.create_account(email, password)

        billing_address_page = BillingAddressPage(self.driver)

        billing_address_page.open_edit_billing_address()
        billing_address_page.set_personal_data("John", "Doe")
        billing_address_page.select_county("Poland")
        billing_address_page.set_address("Kwiatowa 1", "01-001", "Warsow")
        billing_address_page.set_phone_nuber("777777777")
        billing_address_page.save_address()
        assert "Address changed successfully" in billing_address_page.get_message_text()
