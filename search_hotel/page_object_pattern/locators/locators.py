class SearchHotelLocators:
    
    searchbox_span = "//div[@id='s2id_autogen8']//span[@class='select2-chosen']"
    searchbox_input = "//div[contains(@class, 'select2-drop-active')]//input"
    searchbox_result_ul = "//ul[@class='select2-result-sub']"
    check_in_input = "//input[@name='checkin']"
    next_th = "//div[9]/div[1]//tr[1]/th[@class='next']"
    day_in_td = "//div[9]/div[1]//tr/td[@class='day ']"
    day_out_td = "//div[10]/div[1]//tr/td[@class='day ']"
    travellers_input = "//input[@id='travellersInput']"
    adult_input = "//input[@id='adultInput']"
    child_input = "//input[@id='childInput']"
    search_button = "//button[contains(@class, 'btn-primary pfb0 loader')]"

class SearchResultsLocators:

    hotel_names = "//h4[contains(@class, 'list_title')]//b"
    hotel_prices = "//div[contains(@class, 'price_tab')]//b"
