import allure

from pages.basket_page import BasketPage
from tests_basket_page.data import COUNT_PRODUCT


class TestBasketItemCountDisplayed:
    @allure.title("Проверка, что в корзине отображается количество товаров")
    def test_basket_item_count_displayed(self, browser):
        basket_item_count = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            basket_item_count.open_basket()
        with allure.step("Проверяем, что количество товаров в корзине отображается"):
            assert basket_item_count.get_text_count_products_basket() == COUNT_PRODUCT
