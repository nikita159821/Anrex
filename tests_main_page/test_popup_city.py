import allure

from pages.anrex_main_page import MainPage
from tests_main_page.data import CITY_TITLE


class TestPopup:

    @allure.title('В списке выбора города отображается тайтл "Выберите Ваш регион"')
    def test_popup_city(self, browser):
        popup_city = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            popup_city.open()
        with allure.step('Нажимаем на выбранный город на сайте'):
            popup_city.city_wrap_click()
        with allure.step('Проверяем, что отображается тайтл "Выберите Ваш регион"'):
            assert popup_city.popup_city() == CITY_TITLE
