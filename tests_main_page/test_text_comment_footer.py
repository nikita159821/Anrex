import allure

from pages.anrex_main_page import MainPage
from tests_main_page.data import TEXT_COMMENT


class TestCommentFooter:

    @allure.title('В футере отображается наименование организации')
    def test_text_comment_footer(self, browser):
        comment_footer = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            comment_footer.open()
        with allure.step('Скроллим до футера'):
            comment_footer.get_section_footer()
        with allure.step('Проверяем, что в футере отображается информация для покупателей'):
            assert comment_footer.get_text_comment() == TEXT_COMMENT
