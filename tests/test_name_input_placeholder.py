from pages.anrex_main_page import MainPage
from tests.data import NAME_PLACEHOLDER


class TestInputNamePlaceholder:
    def test_name_input_placeholder(self, browser):
        name_placeholder = MainPage(browser)
        name_placeholder.open()
        name_placeholder.city_wrap_click()
        name_placeholder = name_placeholder.get_name_input_placeholder()
        assert NAME_PLACEHOLDER == name_placeholder
