import allure

from pages.anrex_main_page import MainPage


class TestInputName:

    @allure.title('В модальном окне "Заказать обратный звонок" отображается инпут "Ваше имя"')
    def test_callback_popup_name_input(self, browser):
        name_input = MainPage(browser)
        name_input.open()
        name_input.click_callback_link()
        assert name_input.get_callback_popup_name_input().is_displayed()
