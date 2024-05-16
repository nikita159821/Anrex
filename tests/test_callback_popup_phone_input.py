import allure

from pages.anrex_main_page import MainPage


class TestInputPhone:

    @allure.title('В модальном окне "Заказать обратный звонок" отображается инпут "Ваш телефон"')
    def test_callback_popup_phone_input(self, browser):
        phone_input = MainPage(browser)
        phone_input.open()
        phone_input.click_callback_link()
        assert phone_input.get_callback_popup_phone_input().is_displayed()
