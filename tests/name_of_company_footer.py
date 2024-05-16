from pages.anrex_main_page import MainPage
from tests.data import COMPANY_FOOTER
import allure


class TestFooterCompany:

    @allure.title('В футере отображается наименование организации')
    def test_name_of_company_footer(self, browser):
        company_footer = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            company_footer.open()
        with allure.step('Получаем наименование организации и сравниваем'):
            assert company_footer.get_text_footer() == COMPANY_FOOTER
