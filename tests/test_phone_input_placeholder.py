import allure

from pages.anrex_main_page import MainPage
from tests.data import PHONE_PLACEHOLDER


class TestInputPhonePlaceholder:

    @allure.title('В форме "Заявка на обратный звонок", в поле "Ваш телефон" отображается плейсхолдер')
    def test_phone_input_placeholder(self, browser):
        phone_placeholder = MainPage(browser)
        phone_placeholder.open()
        phone_placeholder.city_wrap_click()
        assert phone_placeholder.get_phone_input_placeholder() == PHONE_PLACEHOLDER
