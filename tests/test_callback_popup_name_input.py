from pages.anrex_main_page import MainPage


class TestInputName:
    def test_callback_popup_name_input(self, browser):
        name_input = MainPage(browser)
        name_input.open()
        name_input.city_wrap_click()
        assert not  name_input.get_callback_popup_name_input().is_displayed()
