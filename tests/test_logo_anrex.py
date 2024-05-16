import allure

from pages.anrex_main_page import MainPage
from tests.data import EXPECTED_LOGO_SRC


class TestLogo:

    @allure.title('В шапке сайта отображается логотип "Anrex"')
    def test_logo(self, browser):
        anrex_page = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            anrex_page.open()
        with allure.step('Получаем и сохраняем ссылку на img. И сравниваем ссылку с ожидаемой'):
            assert anrex_page.get_logo_src() == EXPECTED_LOGO_SRC
