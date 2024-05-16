import allure

from pages.anrex_main_page import MainPage
from tests.data import CITY


class TestCityIsChelyabinsk:
    @allure.title('Выбранный город Москва на сайте отображается первым в списке городов в модальном окне')
    def test_first_city_is_Moscow(self, browser):
        first_city = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            first_city.open()
        with allure.step('Нажимаем на город на сайте'):
            first_city.city_wrap_click()
        with allure.step('Находим первый город в модальном окне и сравниваем с ожидаемым'):
            assert first_city.first_sity() == CITY
