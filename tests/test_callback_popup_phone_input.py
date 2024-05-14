from pages.anrex_main_page import MainPage


class TestInputPhone:
    def test_callback_popup_phone_input(self, browser):
        phone_input = MainPage(browser)
        phone_input.open()
        phone_input.city_wrap_click()
        assert not phone_input.get_callback_popup_phone_input().is_displayed()
