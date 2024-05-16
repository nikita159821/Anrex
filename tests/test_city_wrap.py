import allure

from pages.anrex_main_page import MainPage


class TestCity:

    @allure.title('В шапке сайта отображается выбранный город')
    def test_sity(self, browser):
        sity = MainPage(browser)
        sity.open()
        assert sity.city_wrap().is_displayed()
