import allure

from pages.anrex_main_page import MainPage
from tests.data import SALE
from tests.urls import URL, CHAPTER_SALE, CHAPTER_CATALOG


class TestHeaderSale:

    @allure.title('Проверка, что отображается раздел "Скидки" в шапке сайта')
    def test_header_sale_visibility(self, browser):
        sale_visibility = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            sale_visibility.open()
        with allure.step('Находим раздел "Скидки" в шапке сайта и сравниваем с ожидаемым'):
            assert sale_visibility.get_sale_text() == SALE

    @allure.title('По клику на раздел "Скидки", редирект в "Каталог"')
    def test_redirection_catalog(self, browser):
        redirection_catalog = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            redirection_catalog.open()
        with allure.step('Нажимаем на раздел "Скидки"'):
            redirection_catalog.click_sale()
        with allure.step('Проверяем, что открылась страница "Скидки"'):
            assert redirection_catalog.get_current_url() == f'{URL}{CHAPTER_CATALOG}{CHAPTER_SALE}'