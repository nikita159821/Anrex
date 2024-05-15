from pages.anrex_main_page import MainPage
from tests.data import HOVER


class TestHover:

    def test_hover(self, browser):
        hover = MainPage(browser)
        hover.open()
        assert hover.get_hover_tooltip_text() == HOVER
