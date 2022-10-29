import pytest
import allure

from search_hotel.page_object_pattern.pages.search_hotel import SearchHotelPage
from search_hotel.page_object_pattern.pages.search_results import SearchResultsPage


@pytest.mark.usefixtures("setup")
class TestHotelSearch:

    @allure.title("This is title.")
    @allure.description("This is description.")
    def test_hotel_search(self, setup):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city("Dubai")
        search_hotel_page.set_date_range(1, 1)
        search_hotel_page.set_travellers("2", "2")
        search_hotel_page.perform_serach()
        result_page = SearchResultsPage(self.driver)
        hotel_names = result_page.get_hotel_names()
        hotel_prices = result_page.get_hotel_prices()
        assert hotel_names[0] == "Jumeirah Beach Hotel"
        assert hotel_names[1] == "Oasis Beach Tower"
        assert hotel_names[2] == "Rose Rayhaan Rotana"
        assert hotel_names[3] == "Hyatt Regency Perth"
        assert hotel_prices[0] == "$22"
        assert hotel_prices[1] == "$50"
        assert hotel_prices[2] == "$80"
        assert hotel_prices[3] == "$150"
