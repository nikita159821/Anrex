import time

from pages.anrex_main_page import MainPage
from tests.data import SEARCH


class TestDisplaysSearch:

    # Проверка, что отображается иконка в шапке сайта
    def test_header_displays_search(self, browser):
        displays_search = MainPage(browser)
        displays_search.open()
        svg_xmlns = displays_search.get_search_cvg()
        assert svg_xmlns == SEARCH

    # Проверка отображение строки поиска в шапке сайта.
    def test_search_click(self, browser):
        search_click = MainPage(browser)
        search_click.open()
        search_click.get_search_click()
        search_line = search_click.get_search_input()
        assert search_line.is_displayed()

    def test_search_click_close(self, browser):
        search_click_close = MainPage(browser)
        search_click_close.open()
        search_click_close.get_search_click()
        search_click_close.get_search_click()
        time.sleep(8)
        search_line = search_click_close.get_search_input()
        assert search_line is None
