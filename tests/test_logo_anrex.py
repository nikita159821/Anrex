from pages.anrex_main_page import MainPage
from tests.data import EXPECTED_LOGO_SRC


class TestLogo:
    def test_logo(self, browser):
        anrex_page = MainPage(browser)
        # Открываем страницу
        anrex_page.open()
        # Получаем и сохраняем ссылку на img
        assert anrex_page.get_logo_src() == EXPECTED_LOGO_SRC
