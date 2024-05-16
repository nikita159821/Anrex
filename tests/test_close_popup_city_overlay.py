import allure

from pages.anrex_main_page import MainPage


class TestClosePopupOverlay:
    @allure.title('Модальное окно с выбором города закрывается через оверлей')
    def test_close_popup_city_overlay(self, browser):
        close_popup = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            close_popup.open()
        with allure.step('Нажимаем на город в шапке сайта'):
            close_popup.city_wrap_click()
        with allure.step('Нажимаем вне модального окна'):
            close_popup.slider_click()
        with allure.step('Проверяем, что модальное окно закрыто. Если получен тайтл - окно закрыто'):
            assert close_popup.get_title_sale().is_displayed()
