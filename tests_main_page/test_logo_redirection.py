import allure

from pages.anrex_main_page import MainPage
from tests_main_page.urls import URL


class TestLogoRedirection:

    @allure.title('По нажатию на лого в шапке, открывается главная страница сайта')
    def test_logo_redirects_to_home(self, browser):
        logo_redirects = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            logo_redirects.open()
        with allure.step('Нажимаем на логотип в шапке страницы'):
            logo_redirects.logo_click()
        with allure.step('Сравниваем полученный URL с ожидаемым URL'):
            assert logo_redirects.get_current_url() == URL
