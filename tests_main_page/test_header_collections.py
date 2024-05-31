import allure

from pages.anrex_main_page import MainPage
from tests_main_page.data import COLLECTIONS
from tests_main_page.urls import URL, CHAPTER_COLLECTIONS


class TestHeaderCollections:

    @allure.title('Проверка, что отображается раздел "Коллекции" в шапке сайта')
    def test_header_collections_visibility(self, browser):
        collections_visibility = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            collections_visibility.open()
        with allure.step('Получаем текст раздела "Коллекции"'):
            assert collections_visibility.get_collections_text() == COLLECTIONS

    @allure.title('Проверка, открытия раздела "Коллекции" в шапке сайта')
    def test_header_collections_section_opens(self, browser):
        section_opens = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            section_opens.open()
        with allure.step('Открываем раздел "Коллекции"'):
            section_opens.click_collections()
        with allure.step('Проверяем открытие раздела "Коллекции"'):
            assert section_opens.get_current_url() == f'{URL}{CHAPTER_COLLECTIONS}'
