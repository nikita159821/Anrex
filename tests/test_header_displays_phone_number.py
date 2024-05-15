from pages.anrex_main_page import MainPage
from tests.data import DISPLAYS_PHONE


class TestDisplaysPhone:
    def test_header_displays_phone_number(self, browser):
        displays_phone = MainPage(browser)
        displays_phone.open()
        assert displays_phone.get_phone_callback() == DISPLAYS_PHONE
