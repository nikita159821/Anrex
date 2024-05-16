import allure

from pages.anrex_main_page import MainPage
from tests.data import EXPECTED_LOGO_SRC


class TestLogo:

    @allure.title('В шапке сайта отображается логотип "Anrex"')
    def test_logo(self, browser):
        anrex_page = MainPage(browser)
        anrex_page.open()
        # Получаем и сохраняем ссылку на img
        assert anrex_page.get_logo_src() == EXPECTED_LOGO_SRC
