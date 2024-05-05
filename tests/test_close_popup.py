import time

from pages.anrex_main_page import MainPage


class TestClosePopup:
    def test_close_popup(self, browser):
        close_popup = MainPage(browser)
        close_popup.open()
        close_popup.city_wrap_click()
        time.sleep(10)
        close = close_popup.city_wrap()
        assert close.is_displayed()
