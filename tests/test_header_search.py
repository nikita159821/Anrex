import allure

from pages.anrex_main_page import MainPage
from tests.data import SEARCH


class TestDisplaysSearch:

    @allure.title('Проверка, что отображается иконка поиска в шапке сайта')
    def test_header_displays_search(self, browser):
        displays_search = MainPage(browser)
        displays_search.open()
        assert displays_search.get_search_cvg() == SEARCH

    @allure.title('Проверка отображение строки поиска в шапке сайта.')
    def test_search_click(self, browser):
        search_click = MainPage(browser)
        search_click.open()
        search_click.get_search_click()
        assert search_click.get_search_input().is_displayed()

    @allure.title('По нажатию строка поиска закрывается')
    def test_search_click_close(self, browser):
        search_click_close = MainPage(browser)
        search_click_close.open()
        search_click_close.get_search_click()
        search_click_close.get_search_active()
        assert not search_click_close.get_search_input().is_displayed()

