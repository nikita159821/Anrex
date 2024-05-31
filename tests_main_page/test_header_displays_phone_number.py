import allure

from pages.anrex_main_page import MainPage
from tests.data import DISPLAYS_PHONE


class TestDisplaysPhone:

    @allure.title('В шапке сайта отображается номер телефона')
    def test_header_displays_phone_number(self, browser):
        displays_phone = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            displays_phone.open()
        with allure.step('Находим номер телефона в шапке сайта и сравниваем с ожидаемым'):
            assert displays_phone.get_phone_callback() == DISPLAYS_PHONE
