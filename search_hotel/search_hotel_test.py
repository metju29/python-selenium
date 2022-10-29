from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(10)
driver.get("http://www.kurs-selenium.pl/demo/")
driver.maximize_window()

driver.find_element(By.XPATH, "//div[@id='s2id_autogen8']//span[@class='select2-chosen']").click()
driver.find_element(By.XPATH, "//div[contains(@class, 'select2-drop-active')]//input").send_keys("Dubai")
driver.find_element(By.XPATH, "//ul[@class='select2-result-sub']").click()
# driver.find_element(By.XPATH, "//input[@name='checkin']").send_keys("26/10/2022")
# driver.find_element(By.XPATH, "//input[@name='checkout']").send_keys("29/10/2022")
driver.find_element(By.XPATH, "//input[@name='checkin']").click()
driver.find_element(By.XPATH, "//td[@class='day ' and text()='26']").click()
elements = driver.find_elements(By.XPATH, "//td[@class='day ' and text()='29']")
for element in elements:
    if element.is_displayed():
        element.click()
        break
driver.find_element(By.XPATH, "//input[@id='travellersInput']").click()
driver.find_element(By.XPATH, "//input[@id='adultInput']").clear()
driver.find_element(By.XPATH, "//input[@id='adultInput']").send_keys("4")
driver.find_element(By.XPATH, "//input[@id='childInput']").clear()
driver.find_element(By.XPATH, "//input[@id='childInput']").send_keys("4")
driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary pfb0 loader')]").click()
hotels = driver.find_elements(By.XPATH, "//h4[contains(@class, 'list_title')]//b")
hotel_names = [hotel.get_attribute("textContent") for hotel in hotels]
for name in hotel_names:
    print("Hotel name: " + name)
prices = driver.find_elements(By.XPATH, "//div[contains(@class, 'price_tab')]//b")
price_values = [price.get_attribute("textContent") for price in prices]
for price in price_values:
    print("Price is: " + price)

assert hotel_names[0] == "Jumeirah Beach Hotel"
assert hotel_names[1] == "Oasis Beach Tower"
assert hotel_names[2] == "Rose Rayhaan Rotana"
assert hotel_names[3] == "Hyatt Regency Perth"

assert price_values[0] == "$22"
assert price_values[1] == "$50"
assert price_values[2] == "$80"
assert price_values[3] == "$150"

driver.quit()