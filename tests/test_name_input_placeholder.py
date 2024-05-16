import allure

from pages.anrex_main_page import MainPage
from tests.data import NAME_PLACEHOLDER


class TestInputNamePlaceholder:

    @allure.title('В форме "Заявка на обратный звонок", в поле "Ваше имя" отображается плейсхолдер')
    def test_name_input_placeholder(self, browser):
        name_placeholder = MainPage(browser)
        name_placeholder.open()
        name_placeholder.city_wrap_click()
        assert name_placeholder.get_name_input_placeholder() == NAME_PLACEHOLDER
