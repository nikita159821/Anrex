from pages.anrex_main_page import MainPage
from tests.data import TITLE_VALENCIA, TITLE_JAZZ


class TestHomepageCollections:

    # На главной странице отображается блок "Наши коллекции"
    def test_homepage_collections_is_displayed(self, browser):
        homepage_collections = MainPage(browser)
        homepage_collections.open()
        assert homepage_collections.get_section_collections().is_displayed()

    # Переключение коллекций в карусели через стрелку вправо

    def test_switch_carousel_collections_right(self, browser):
        collections_right = MainPage(browser)
        collections_right.open()
        collections_right.get_section_collections()
        collections_right.click_button_right()
        assert collections_right.collections_title_jazz() == TITLE_JAZZ

    # Переключение коллекций в карусели через стрелку влево
    def test_switch_carousel_collections_left(self, browser):
        collections_left = MainPage(browser)
        collections_left.open()
        collections_left.get_section_collections()
        collections_left.click_button_left()
        assert collections_left.collections_title_valencia() == TITLE_VALENCIA

