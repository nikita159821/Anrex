import allure

from pages.anrex_main_page import MainPage
from tests.data import TITLE_VALENCIA, TITLE_JAZZ, TITLE_BUTTON, TITLE_BUTTON_VIEW_COLLECTIONS
from tests.urls import URL, COLLECTIONS_JAGGER, CHAPTER_COLLECTIONS


class TestHomepageCollections:

    @allure.title('На главной странице отображается блок "Наши коллекции"')
    def test_homepage_collections_is_displayed(self, browser):
        homepage_collections = MainPage(browser)
        homepage_collections.open()
        assert homepage_collections.get_section_collections().is_displayed()

    @allure.title('Переключение коллекций в карусели через стрелку вправо')
    def test_switch_carousel_collections_right(self, browser):
        collections_right = MainPage(browser)
        collections_right.open()
        collections_right.get_section_collections()
        collections_right.click_button_right()
        assert collections_right.collections_title_jazz() == TITLE_JAZZ

    @allure.title('Переключение коллекций в карусели через стрелку влево')
    def test_switch_carousel_collections_left(self, browser):
        collections_left = MainPage(browser)
        collections_left.open()
        collections_left.get_section_collections()
        collections_left.click_button_left()
        assert collections_left.collections_title_valencia() == TITLE_VALENCIA

    @allure.title('В блоке "Наши коллекции" отображается кнопка "Смотреть коллекцию"')
    def test_collection_button_is_displayed(self, browser):
        button_is_displayed = MainPage(browser)
        button_is_displayed.open()
        button_is_displayed.get_section_collections()
        assert button_is_displayed.get_button_text_collections() == TITLE_BUTTON

    @allure.title('Редирект в коллекцию, по нажатию на кнопку "Смотреть коллекцию"')
    def test_redirect_collection_button(self, browser):
        redirect_collection = MainPage(browser)
        redirect_collection.open()
        redirect_collection.get_section_collections()
        redirect_collection.get_click_button_collections()
        assert redirect_collection.get_current_url() == f'{URL}{CHAPTER_COLLECTIONS}{COLLECTIONS_JAGGER}'

    @allure.title('Под блоком "Наши коллекции" отображается кнопка "Смотреть все коллекции"')
    def test_display_view_all_collections_button(self, browser):
        collections_button = MainPage(browser)
        collections_button.open()
        collections_button.get_section_collections()
        assert collections_button.get_button_text_view_collections() == TITLE_BUTTON_VIEW_COLLECTIONS

    @allure.title('Редирект в коллекции, по нажатию на кнопку "Смотреть все коллекции"')
    def test_redirect_collections_button(self,browser):
        redirect_collection = MainPage(browser)
        redirect_collection.open()
        redirect_collection.get_section_collections()
        redirect_collection.get_click_button_view_collections()
        assert redirect_collection.get_current_url() == f'{URL}{CHAPTER_COLLECTIONS}'
