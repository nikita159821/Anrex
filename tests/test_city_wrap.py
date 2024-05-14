from pages.anrex_main_page import MainPage


class TestCity:
    def test_sity(self, browser):
        sity = MainPage(browser)
        sity.open()
        assert sity.city_wrap().is_displayed()
