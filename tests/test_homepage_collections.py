import time

from pages.anrex_main_page import MainPage
from tests.data import TITLE_VALENCIA, TITLE_JAZZ, TITLE_BUTTON


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

    # В блоке "Наши коллекции" отображается кнопка "Смотреть коллекцию"
    def test_collection_button_is_displayed(self, browser):
        button_is_displayed = MainPage(browser)
        button_is_displayed.open()
        button_is_displayed.get_section_collections()
        assert button_is_displayed.get_button_collections() == TITLE_BUTTON
