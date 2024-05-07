import time

from pages.anrex_main_page import MainPage


class TestClosePopupOverlay:
    def test_close_popup_city_overlay(self, browser):
        close_popup = MainPage(browser)
        close_popup.open()
        close_popup.city_wrap_click()
        close_popup.slider_click()
        print('закрыли')
        time.sleep(20)
        popup_city = close_popup.popup_city()
        assert not popup_city.is_displayed()
