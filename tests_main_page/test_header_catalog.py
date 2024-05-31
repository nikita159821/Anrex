import allure

from locators.main_page_locators import catalog, by_type_of_furniture_and_room
from pages.anrex_main_page import MainPage
from tests.data import CATALOG, FURNITURE_AND_ROOM
from tests.urls import URL, CHAPTER_TUMBY, CHAPTER_CATALOG


class TestHeaderCatalog:

    @allure.title('Проверка, что отображается раздел "Каталог" в шапке сайта')
    def test_header_catalog_visibility(self, browser):
        catalog_visibilit = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            catalog_visibilit.open()
        with allure.step('Получаем текст раздела "Каталог" и сравниваем с ожидаемым'):
            assert catalog_visibilit.get_catalog_text() == CATALOG

    @allure.title('Проверка, что при наведении на раздел "Каталог", появляется выпадающий список')
    def test_catalog_hover_displays_dropdown(self, browser):
        displays_dropdown = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            displays_dropdown.open()
        with allure.step('Наводим курсор на раздел "Каталог"'):
            displays_dropdown.move_cursor_to_element(catalog)
        with allure.step('Получаем список разделов и сравниваем с ожидаемым'):
            assert displays_dropdown.get_elements_text_header(by_type_of_furniture_and_room) == FURNITURE_AND_ROOM

    @allure.title('Проверка, что при снятии фокуса с раздела "Каталог", выпадающий список закрывается')
    def test_catalog_dropdown_closes_on_focus_loss(self, browser):
        closes_on_focus = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            closes_on_focus.open()
        with allure.step('Наводим курсор на раздел "Каталог"'):
            closes_on_focus.move_cursor_to_element(catalog)
        with allure.step('Снимаем курсор с раздела "Каталог"'):
            closes_on_focus.defocus_element()
        with allure.step('Проверяем, что список разделов не отображается. Сравниваем список с ожидаемым'):
            assert closes_on_focus.get_elements_text_header('') == []

    @allure.title('Проверка, открытия раздела "Тумбы" через "Каталог"')
    def test_catalog_chests_section(self, browser):
        chests_section = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            chests_section.open()
        with allure.step('Наводим курсор на раздел "Каталог"'):
            chests_section.move_cursor_to_element(catalog)
        with allure.step('Нажимаем на раздел "Тумбы"'):
            chests_section.click_tumby()
        with allure.step('Проверяем переход в раздел "Тумбы"'):
            assert chests_section.get_current_url() == f'{URL}{CHAPTER_CATALOG}{CHAPTER_TUMBY}'

    @allure.title('Проверка, открытия раздела "Смотреть всё" через "Каталог"')
    def test_catalog_all_section_opens(self, browser):
        section_opens = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            section_opens.open()
        with allure.step('Наводим курсор на раздел "Каталог"'):
            section_opens.move_cursor_to_element(catalog)
        with allure.step('Нажимаем на раздел "Смотреть всё"'):
            section_opens.click_see_all()
        with allure.step('Проверяем переход в раздел "Каталог"'):
            assert section_opens.get_current_url() == f'{URL}{CHAPTER_CATALOG}'
