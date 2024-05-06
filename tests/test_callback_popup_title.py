from pages.anrex_main_page import MainPage
from tests.data import TITLE_BACK_CALL, CALLBACK_POPUP_TITLE


class TestPopupTitle:
    def test_callback_popup_title(self, browser):
        title_back = MainPage(browser)
        title_back.open()
        title_back.click_callback_link()
        actual_title_text = title_back.get_callback_popup_title()
        assert CALLBACK_POPUP_TITLE == actual_title_text
