import allure

from pages.anrex_main_page import MainPage
from tests.urls import URL


class TestLogoRedirection:

    @allure.title('По нажатию на лого в шапке, открывается главная страница сайта')
    def test_logo_redirects_to_home(self, browser):
        logo_redirects = MainPage(browser)
        logo_redirects.open()
        logo_redirects.logo_click()
        # Сравнимаем полученный URL с ожидаемым URL
        assert logo_redirects.get_current_url() == URL
