import allure

from pages.anrex_main_page import MainPage


class TestClosePopup:

    @allure.title('Модальное окно с выбором города закрывается через крестик')
    def test_close_popup(self, browser):
        close_popup = MainPage(browser)
        close_popup.open()
        close_popup.city_wrap_click()
        close_popup.close_popup_click()
        assert not close_popup.popup_city().is_displayed()
