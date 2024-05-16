import allure

from pages.anrex_main_page import MainPage


class TestInputName:

    @allure.title('В модальном окне "Заказать обратный звонок" отображается инпут "Ваше имя"')
    def test_callback_popup_name_input(self, browser):
        name_input = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            name_input.open()
        with allure.step('Нажимаем на "Заказать обратный звонок"'):
            name_input.click_callback_link()
        with allure.step('Проверяем, что отображается поле "Ваше имя'):
            assert name_input.get_callback_popup_name_input().is_displayed()
