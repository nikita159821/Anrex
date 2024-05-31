import allure

from pages.anrex_main_page import MainPage
from tests_main_page.data import PHONE_PLACEHOLDER


class TestInputPhonePlaceholder:

    @allure.title('В форме "Заявка на обратный звонок", в поле "Ваш телефон" отображается плейсхолдер')
    def test_phone_input_placeholder(self, browser):
        phone_placeholder = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            phone_placeholder.open()
        with allure.step('Нажимаем на "Заказать обратный звонок"'):
            phone_placeholder.click_callback_link()
        with allure.step('Проверяем, что в поле "Ваш телефон" отображается плейсхолдер'):
            assert phone_placeholder.get_phone_input_placeholder() == PHONE_PLACEHOLDER
