import allure

from pages.anrex_main_page import MainPage
from tests.data import NAME_PLACEHOLDER


class TestInputNamePlaceholder:

    @allure.title('В форме "Заявка на обратный звонок", в поле "Ваше имя" отображается плейсхолдер')
    def test_name_input_placeholder(self, browser):
        name_placeholder = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            name_placeholder.open()
        with allure.step('Нажимаем на "Заказать обратный звонок"'):
            name_placeholder.click_callback_link()
        with allure.step('Проверяем, что в поле "Ваше имя" отображается плейсхолдер'):
            assert name_placeholder.get_name_input_placeholder() == NAME_PLACEHOLDER
