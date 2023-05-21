import pytest

from selenium_demo.pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestLogIn:

    def test_log_in_passed(self):
        my_acc_page = MyAccountPage(self.driver)

        username = "test@szkolenie.pl"
        password = "TestTestTest12345#"

        my_acc_page.open_page()
        my_acc_page.log_in(username, password)
        assert my_acc_page.is_logout_link_displayed()

    def test_log_in_failed(self):
        my_acc_page = MyAccountPage(self.driver)

        username = "test@szkolenie.pl"
        password = "TestTestTest#"

        my_acc_page.open_page()
        my_acc_page.log_in(username, password)
        msg1 = "ERROR: Incorrect username or password."
        msg2 = "ERROR: Too many failed login attempts."
        assert msg1 or msg2 in my_acc_page.get_error_msg()
