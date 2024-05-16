import allure

from pages.anrex_main_page import MainPage


class TestCity:

    @allure.title('В шапке сайта отображается выбранный город')
    def test_sity(self, browser):
        sity = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            sity.open()
        with allure.step('Находим и проверяем отображение выбранного города в шапке сайта'):
            assert sity.city_wrap().is_displayed()
