import pytest

from selenium_demo.pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestCreateAccount:

    def test_create_account_failed(self):
        my_acc_page = MyAccountPage(self.driver)

        email = "test@szkolenie.pl"
        password = "TestTestTest12345#"

        my_acc_page.open_page()
        my_acc_page.create_account(email, password)
        msg = "An account is already registered with your email address. Please log in."
        assert msg in my_acc_page.get_error_msg()

    def test_create_account_passed(self):
        my_acc_page = MyAccountPage(self.driver)

        email = my_acc_page.get_random_email()
        password = "TestTestTest12345#"

        my_acc_page.open_page()
        my_acc_page.create_account(email, password)
        assert my_acc_page.is_logout_link_displayed()
