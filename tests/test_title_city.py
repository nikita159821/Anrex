import allure

from pages.anrex_main_page import MainPage


class TestCity:

    @allure.title('В модальном окне выбора города отображается тайтл "Выберите Ваш регион"')
    def test_title_city(self, browser):
        popup_city = MainPage(browser)
        popup_city.open()
        popup_city.city_wrap_click()
        assert popup_city.popup_city().is_displayed()
