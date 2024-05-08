from pages.anrex_main_page import MainPage
from tests.data import SEARCH


class TestDisplaysSearch:
    def test_header_displays_search(self, browser):
        displays_search = MainPage(browser)
        displays_search.open()
        svg_xmlns = displays_search.get_search_cvg()
        assert svg_xmlns == SEARCH

    def test_search_click(self, browser):
        search_click = MainPage(browser)
        search_click.open()
        search_click.get_search_click()
        search_line = search_click.get_search_input()
        assert search_line.is_displayed()
