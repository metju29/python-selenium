from selenium.webdriver.common.by import By


class MainPageLocators:

    my_account_menu_link = (By.CSS_SELECTOR, "li.menu-item-22")


class MyAccountPageLocators:

    username_input = (By.CSS_SELECTOR, "#username")
    password_input = (By.CSS_SELECTOR, "#password")
    login_button = (By.CSS_SELECTOR, "[name=login]")
    reg_email_input = (By.CSS_SELECTOR, "input#reg_email")
    reg_password_input = (By.CSS_SELECTOR, "input#reg_password")
    register_button = (By.CSS_SELECTOR, "button[name=register]")
    logout_link = (By.CSS_SELECTOR, "li[class*=customer-logout] a")
    addresses_link = (By.CSS_SELECTOR, "li[class*=edit-address] a")
    woocommerce_error_alert = (By.CSS_SELECTOR, "ul.woocommerce-error li")
    woocommerce_message_alert = (By.CSS_SELECTOR, "div.woocommerce-message")


class EditAddressPageLocators:

    billing_address_edit_link = (By.CSS_SELECTOR, "div[class*=column1] a.edit")
    billing_first_name_input = (By.CSS_SELECTOR, "#billing_first_name")
    billing_last_name_input = (By.CSS_SELECTOR, "#billing_last_name")
    billing_country_select = (By.CSS_SELECTOR, "#billing_country")
    billing_address_1_input = (By.CSS_SELECTOR, "#billing_address_1")
    billing_postcode_input = (By.CSS_SELECTOR, "#billing_postcode")
    billing_city_input = (By.CSS_SELECTOR, "#billing_city")
    billing_phone_input = (By.CSS_SELECTOR, "#billing_phone")
    save_address_button = (By.CSS_SELECTOR, "[name=save_address]")

class BillingAddressLocators:

    addresses_link = (By.LINK_TEXT, "Addresses")
    edit_link = (By.XPATH, "//div[@class='u-column1 col-1 woocommerce-Address']//a[@class=\"edit\"]")
    first_name_input = (By.ID, "billing_first_name")
    last_name_input = (By.ID, "billing_last_name")
    country_select = (By.ID, "billing_country")
    address_input = (By.ID, "billing_address_1")
    postcode_input = (By.ID, "billing_postcode")
    city_input = (By.ID, "billing_city")
    phone_input = (By.ID, "billing_phone")
    save_address_button = (By.NAME, "save_address")
    message_div = (By.XPATH, "//div[@class=\"woocommerce-message\"]")
