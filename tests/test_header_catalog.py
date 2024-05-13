from locators.main_page_locators import catalog, by_type_of_furniture_and_room
from pages.anrex_main_page import MainPage
from tests.data import CATALOG, FURNITURE_AND_ROOM
from tests.urls import URL, CHAPTER_TUMBY, CHAPTER_CATALOG


class TestHeaderCatalog:

    # Проверка, что отображается раздел "Каталог" в шапке сайта
    def test_header_catalog_visibility(self, browser):
        catalog_visibilit = MainPage(browser)
        catalog_visibilit.open()
        assert catalog_visibilit.get_catalog_text() == CATALOG

    # Проверка, что при наведении на раздел "Каталог", появляется выпадающий список
    def test_catalog_hover_displays_dropdown(self, browser):
        displays_dropdown = MainPage(browser)
        displays_dropdown.open()
        displays_dropdown.move_cursor_to_element(catalog)
        assert displays_dropdown.get_elements_text(by_type_of_furniture_and_room) == FURNITURE_AND_ROOM

    # Проверка, что при снятии фокуса с раздела "Каталог", выпадающий список закрывается
    def test_catalog_dropdown_closes_on_focus_loss(self, browser):
        closes_on_focus = MainPage(browser)
        closes_on_focus.open()
        closes_on_focus.move_cursor_to_element(catalog)
        closes_on_focus.defocus_element()
        assert closes_on_focus.get_type_of_furniture_and_room() == ['']

    # Проверка, открытия раздела "Тумбы" через "Каталог"
    def test_catalog_chests_section(self, browser):
        chests_section = MainPage(browser)
        chests_section.open()
        chests_section.move_cursor_to_element(catalog)
        chests_section.send_keys_tumby()
        assert chests_section.get_current_url() == f'{URL}{CHAPTER_CATALOG}{CHAPTER_TUMBY}'
