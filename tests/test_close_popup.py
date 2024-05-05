import time

from pages.anrex_main_page import MainPage


class TestClosePopup:
    def test_close_popup(self, browser):
        close_popup = MainPage(browser)
        close_popup.open()
        close_popup.city_wrap_click()
        close_popup.close_popup_click()
        city_wrap = close_popup.city_wrap()
        assert city_wrap.is_displayed()
