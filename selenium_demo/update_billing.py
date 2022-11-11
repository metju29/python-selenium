import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

import logging

logger = logging.getLogger(__name__)


def test_update_billing_address():
    number = str(random.randint(0, 10000))
    email = f"test{number}@szkolenie.pl"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("http://seleniumdemo.com/?page_id=7")
    logger.info(f"Test for e-mail adress: {email}")
    driver.find_element(By.ID, "reg_email").send_keys(email)
    driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.ID, "reg_password"))
    driver.find_element(By.ID, "reg_password").send_keys("TestTestTest12345#")
    driver.find_element(By.NAME, "register").click()
    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()
    logger.info("Register passed")
    driver.find_element(By.LINK_TEXT, "Addresses").click()
    driver.find_element(By.XPATH, "//div[@class='u-column1 col-1 woocommerce-Address']//a[@class=\"edit\"]").click()
    driver.find_element(By.ID, "billing_first_name").send_keys("Użytkownik")
    driver.find_element(By.ID, "billing_last_name").send_keys("Testowy")
    Select(driver.find_element(By.ID, "billing_country")).select_by_visible_text("Poland")
    driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.ID, "billing_address_1"))
    driver.find_element(By.ID, "billing_address_1").send_keys("Aleja Testowa 15")
    driver.find_element(By.ID, "billing_postcode").send_keys("00-001")
    driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.ID, "billing_city"))
    driver.find_element(By.ID, "billing_city").send_keys("Warszawa")
    driver.find_element(By.ID, "billing_phone").send_keys("111111111")
    driver.find_element(By.NAME, "save_address").click()
    msg = "Address changed successfully"
    assert msg in driver.find_element(By.XPATH, "//div[@class=\"woocommerce-message\"]").text
    logger.info("Update billing address passed")
