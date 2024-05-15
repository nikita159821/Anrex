from pages.anrex_main_page import MainPage
from tests.data import COMPANY_FOOTER


class TestFooterCompany:

    # В футере отображается наименование организации
    def test_name_of_company_footer(self, browser):
        company_footer = MainPage(browser)
        company_footer.open()
        assert company_footer.get_text_footer() == COMPANY_FOOTER
