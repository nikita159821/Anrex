from pages.anrex_main_page import MainPage
from tests.data import TEXT_COMMENT


class TestCommentFooter:

    # В футере отображается наименование организации
    def test_text_comment_footer(self, browser):
        comment_footer = MainPage(browser)
        comment_footer.open()
        comment_footer.get_section_footer()
        assert comment_footer.get_text_comment() == TEXT_COMMENT
