import allure

from pages.anrex_main_page import MainPage


class TestInputPhone:

    @allure.title('В модальном окне "Заказать обратный звонок" отображается инпут "Ваш телефон"')
    def test_callback_popup_phone_input(self, browser):
        phone_input = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            phone_input.open()
        with allure.step('Нажимаем на "Заказать обратный звонок"'):
            phone_input.click_callback_link()
        with allure.step('Проверяем, что отображается поле "Ваш телефон'):
            assert phone_input.get_callback_popup_phone_input().is_displayed()
