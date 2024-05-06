from pages.anrex_main_page import MainPage
from tests.data import TITLE_BACK_CALL


class TestTitle:
    def test_title_back_call(self, browser):
        title_back = MainPage(browser)
        title_back.open()
        title_back.click_callback_link()
        actual_title_text = title_back.get_back_call()
        assert TITLE_BACK_CALL == actual_title_text
