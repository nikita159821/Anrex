import allure

from pages.basket_page import BasketPage
from tests_main_page.urls import URL, BASKET


class TestCatalogToBasket:

    @allure.title('Переход в корзину из каталога')
    def test_catalog_to_basket(self, browser):
        catalog_to_basket = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            catalog_to_basket.open_basket()
        with allure.step('Проверяем, что открылась страница корзины'):
            assert catalog_to_basket.get_current_url() == f'{URL}{BASKET}'
