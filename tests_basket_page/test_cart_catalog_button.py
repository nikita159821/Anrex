import allure

from pages.basket_page import BasketPage
from tests_main_page.urls import URL, BASKET, CHAPTER_CATALOG


class TestCartCatalogButton:

    @allure.title('Переход в каталог из корзины по кнопке "Начать покупки"')
    def test_cart_catalog_button(self, browser):
        cart_catalog_button = BasketPage(browser)
        with allure.step('Открываем страницу с корзиной'):
            cart_catalog_button.open(f'{URL}{BASKET}')
        with allure.step('Нажимаем "Начать покупки"'):
            cart_catalog_button.click_button_shopping()
        with allure.step('Проверяем, что открылась страница с каталогом'):
            assert cart_catalog_button.get_current_url() == f'{URL}{CHAPTER_CATALOG}'
