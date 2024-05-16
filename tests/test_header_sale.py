import allure

from pages.anrex_main_page import MainPage
from tests.data import SALE
from tests.urls import URL, CHAPTER_SALE, CHAPTER_CATALOG


class TestHeaderSale:

    @allure.title('Проверка, что отображается раздел "Скидки" в шапке сайта')
    def test_header_sale_visibility(self, browser):
        sale_visibility = MainPage(browser)
        sale_visibility.open()
        assert sale_visibility.get_sale_text() == SALE

    @allure.title('По клику на раздел "Скидки", редирект в "Каталог"')
    def test_redirection_catalog(self, browser):
        redirection_catalog = MainPage(browser)
        redirection_catalog.open()
        redirection_catalog.click_sale()
        assert redirection_catalog.get_current_url() == f'{URL}{CHAPTER_CATALOG}{CHAPTER_SALE}'