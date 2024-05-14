from pages.anrex_main_page import MainPage


class TestCallbackLink:

    def test_callback_link(self, browser):
        link = MainPage(browser)
        link.open()
        assert link.get_callback_link().is_displayed()
