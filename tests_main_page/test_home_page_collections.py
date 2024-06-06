import allure

from locators.main_page_locators import button_right, button_left, button_collections, view_collections, \
    section_collections
from pages.anrex_main_page import MainPage
from tests_main_page.data import TITLE_VALENCIA, TITLE_JAZZ, TITLE_BUTTON, TITLE_BUTTON_VIEW_COLLECTIONS
from tests_main_page.urls import URL, COLLECTIONS_JAGGER, CHAPTER_COLLECTIONS


class TestHomepageCollections:

    @allure.title('На главной странице отображается блок "Наши коллекции"')
    def test_homepage_collections_is_displayed(self, browser):
        homepage_collections = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            homepage_collections.open()
        with allure.step('Проверяем, что отображается блок "Наши коллекции"'):
            assert homepage_collections.get_section_collections().is_displayed()

    @allure.title('Переключение коллекций в карусели через стрелку вправо')
    def test_switch_carousel_collections_right(self, browser):
        collections_right = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            collections_right.open()
        with allure.step('Скроллим до блока "Наши коллекции"'):
            collections_right.get_section_collections()
        with allure.step('Добавляем ожидание после скролла'):
            collections_right.wait_for_element(button_right)
        with allure.step('Нажимаем стрелку вправо в разделе "Наши коллекции"'):
            collections_right.click_button_right()
        with allure.step('Добавляем ожидание'):
            collections_right.wait_for_element(button_right)
        with allure.step('Проверяем, что отображается коллекция "Джаз"'):
            assert collections_right.collections_title_jazz() == TITLE_JAZZ

    @allure.title('Переключение коллекций в карусели через стрелку влево')
    def test_switch_carousel_collections_left(self, browser):
        collections_left = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            collections_left.open()
        with allure.step('Скроллим до блока "Наши коллекции"'):
            collections_left.get_section_collections()
        with allure.step('Добавляем ожидание после скролла'):
            collections_left.wait_for_element(button_left)
        with allure.step('Нажимаем стрелку влево в разделе "Наши коллекции"'):
            collections_left.click_button_left()
        with allure.step('Добавляем ожидание'):
            collections_left.wait_for_element(button_left)
        with allure.step('Проверяем, что отображается коллекция "Валенсия"'):
            assert collections_left.collections_title_valencia() == TITLE_VALENCIA

    @allure.title('В блоке "Наши коллекции" отображается кнопка "Смотреть коллекцию"')
    def test_collection_button_is_displayed(self, browser):
        button_is_displayed = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            button_is_displayed.open()
        with allure.step('Скроллим до блока "Наши коллекции"'):
            button_is_displayed.get_section_collections()
        with allure.step('Добавляем ожидание'):
            button_is_displayed.wait_for_element(section_collections)
        with allure.step('Проверяем, что отображается кнопка "Смотреть коллекцию"'):
            assert button_is_displayed.get_button_text_collections() == TITLE_BUTTON

    @allure.title('Редирект в коллекцию, по нажатию на кнопку "Смотреть коллекцию"')
    def test_redirect_collection_button(self, browser):
        redirect_collection = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            redirect_collection.open()
        with allure.step('Скроллим до блока "Наши коллекции"'):
            redirect_collection.get_section_collections()
        with allure.step('Добавляем ожидание после скролла'):
            redirect_collection.wait_for_element(button_collections)
        with allure.step('Нажимаем кнопку "Смотреть коллекцию"'):
            redirect_collection.get_click_button_collections()
        with allure.step('Добавляем ожидание'):
            redirect_collection.wait_for_page_load(f'{URL}{CHAPTER_COLLECTIONS}{COLLECTIONS_JAGGER}')
        with allure.step('Проверяем, что открылась страница с коллекцией "Джаггер"'):
            assert redirect_collection.get_current_url() == f'{URL}{CHAPTER_COLLECTIONS}{COLLECTIONS_JAGGER}'

    @allure.title('Под блоком "Наши коллекции" отображается кнопка "Смотреть все коллекции"')
    def test_display_view_all_collections_button(self, browser):
        collections_button = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            collections_button.open()
        with allure.step('Скроллим до блока "Наши коллекции"'):
            collections_button.get_section_collections()
        with allure.step('Добавляем ожидание после скролла'):
            collections_button.wait_for_element(view_collections)
        with allure.step('Проверяем, что отображается кнопка "Смотреть все коллекции"'):
            assert collections_button.get_button_text_view_collections() == TITLE_BUTTON_VIEW_COLLECTIONS

    @allure.title('Редирект в коллекции, по нажатию на кнопку "Смотреть все коллекции"')
    def test_redirect_collections_button(self,browser):
        redirect_collection = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            redirect_collection.open()
        with allure.step('Скроллим до блока "Наши коллекции"'):
            redirect_collection.get_section_collections()
        with allure.step('Добавляем ожидание после скролла'):
            redirect_collection.wait_for_element(view_collections)
        with allure.step('Нажимаем кнопку "Смотреть все коллекции"'):
            redirect_collection.get_click_button_view_collections()
        with allure.step('Добавляем ожидание'):
            redirect_collection.wait_for_page_load(f'{URL}{CHAPTER_COLLECTIONS}')
        with allure.step('Проверяем, что открылась страница со всеми коллекциями'):
            assert redirect_collection.get_current_url() == f'{URL}{CHAPTER_COLLECTIONS}'
