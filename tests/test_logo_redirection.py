from pages.anrex_main_page import MainPage
from tests.urls import URL


class TestLogoRedirection:
    def test_logo_redirects_to_home(self, browser):
        logo_redirects = MainPage(browser)
        # Открываем страницу
        logo_redirects.open()

        # Нажимаем на логотип anrex
        logo_redirects.logo_click()
        # Сравнимаем полученный URL с ожидаемым URL
        assert logo_redirects.get_current_url() == URL
