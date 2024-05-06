from pages.anrex_main_page import MainPage
from tests.data import PHONE_PLACEHOLDER


class TestInputPhonePlaceholder:
    def test_phone_input_placeholder(self, browser):
        phone_placeholder = MainPage(browser)
        phone_placeholder.open()
        phone_placeholder.city_wrap_click()
        phone_placeholder = phone_placeholder.get_phone_input_placeholder()
        assert PHONE_PLACEHOLDER == phone_placeholder
