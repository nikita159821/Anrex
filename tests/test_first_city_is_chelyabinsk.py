from pages.anrex_main_page import MainPage
from tests.data import CITY


class TestCityIsChelyabinsk:
    def test_first_city_is_chelyabinsk(self, browser):
        first_city = MainPage(browser)
        first_city.open()
        first_city.city_wrap_click()
        assert first_city.first_sity() == CITY
