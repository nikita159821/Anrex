from pages.anrex_main_page import MainPage
from tests.data import COLLECTIONS
from tests.urls import URL, CHAPTER_COLLECTIONS


class TestHeaderCollections:

    # Проверка, что отображается раздел "Коллекции" в шапке сайта
    def test_header_collections_visibility(self, browser):
        collections_visibility = MainPage(browser)
        collections_visibility.open()
        assert collections_visibility.get_collections_text() == COLLECTIONS

    # Проверка, открытия раздела "Коллекции" в шапке сайта
    def test_header_collections_section_opens(self, browser):
        section_opens = MainPage(browser)
        section_opens.open()
        section_opens.click_collections()
        assert section_opens.get_current_url() == f'{URL}{CHAPTER_COLLECTIONS}'
