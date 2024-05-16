import allure

from pages.anrex_main_page import MainPage
from tests.data import LOGO_SRC_FOOTER


class TestLogoFooter:

    @allure.title('В футере сайта отображается логотип "Anrex"')
    def test_logo_footer(self, browser):
        anrex_page = MainPage(browser)
        anrex_page.open()
        assert anrex_page.get_logo_footer_src() == LOGO_SRC_FOOTER
