import allure

from pages.anrex_main_page import MainPage
from tests_main_page.data import LOGO_SRC_FOOTER


class TestLogoFooter:

    @allure.title('В футере сайта отображается логотип "Anrex"')
    def test_logo_footer(self, browser):
        anrex_page = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            anrex_page.open()
        with allure.step('Получаем и сохраняем ссылку на img. И сравниваем ссылку с ожидаемой'):
            assert anrex_page.get_logo_footer_src() == LOGO_SRC_FOOTER
