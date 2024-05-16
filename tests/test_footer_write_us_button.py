import allure

from pages.anrex_main_page import MainPage
from tests.data import TITLE_BUTTON_FOOTER


class TestFooterButton:

    @allure.title('футере отображается кнопка "Написать нам"')
    def test_footer_write_us_button(self, browser):
        write_us_button = MainPage(browser)
        write_us_button.open()
        write_us_button.get_section_footer()
        assert write_us_button.get_text_button_write() == TITLE_BUTTON_FOOTER
