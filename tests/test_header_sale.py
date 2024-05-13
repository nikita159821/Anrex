from pages.anrex_main_page import MainPage
from tests.data import SALE
from tests.urls import URL, CHAPTER_SALE, CHAPTER_CATALOG


class TestHeaderSale:

    # Проверка, что отображается раздел "Скидки" в шапке сайта
    def test_header_delivery_visibility(self, browser):
        delivery_visibility = MainPage(browser)
        delivery_visibility.open()
        assert delivery_visibility.get_sale_text() == SALE

    # По клику на раздел "Скидки", редирект в "Каталог"
    def test_redirection_delivery(self, browser):
        redirection_delivery = MainPage(browser)
        redirection_delivery.open()
        redirection_delivery.click_sale()
        assert redirection_delivery.get_current_url() == f'{URL}{CHAPTER_CATALOG}{CHAPTER_SALE}'