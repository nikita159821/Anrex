import allure

from pages.anrex_main_page import MainPage
from tests.data import CITY_TITLE


class TestClosePopup:

    @allure.title('Модальное окно с выбором города закрывается через крестик')
    def test_close_popup(self, browser):
        close_popup = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            close_popup.open()
        with allure.step('Нажимаем на город в шапке сайта'):
            close_popup.city_wrap_click()
        with allure.step('Нажимаем на крестик в модальном окне выбора города'):
            close_popup.close_popup_click()
        with allure.step('Проверяем, что модальное окно закрыто. Если не получен тайтл - окно закрыто'):
            assert not close_popup.popup_city() == CITY_TITLE
