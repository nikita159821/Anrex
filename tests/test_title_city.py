import allure

from pages.anrex_main_page import MainPage
from tests.data import CITY_TITLE


class TestCity:

    @allure.title('В модальном окне выбора города отображается тайтл "Выберите Ваш регион"')
    def test_title_city(self, browser):
        popup_city = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            popup_city.open()
        with allure.step('Нажимаем на выбранный город на сайте'):
            popup_city.city_wrap_click()
        with allure.step('Проверяем, что в модальном окне есть тайтл "Выберите Ваш регион"'):
            assert popup_city.popup_city() == 'test'
