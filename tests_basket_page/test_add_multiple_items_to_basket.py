import time

import allure

from locators.main_page_locators import button_card
from pages.basket_page import BasketPage
from tests_basket_page.data import COUNT_PRODUCTS


class TestAddMultipleItemsToBasket:
    @allure.title("Проверка добавления нескольких товаров в корзину")
    def test_add_multiple_items_to_basket(self, browser):
        add_multiple_items = BasketPage(browser)
        with allure.step("Открываем страницу с товарами"):
            add_multiple_items.open_catalog()
        with allure.step("Скроллим до карточки товара"):
            add_multiple_items.get_element_scroll_to_element(button_card)
        with allure.step("Добавляем первый товар в корзину"):
            add_multiple_items.button_click_cards()
        with allure.step("Ожидание добавления товара в корзину"):
            add_multiple_items.count_one()
        with allure.step("Добавляем второй товар в корзину"):
            add_multiple_items.button_click_cards()
        with allure.step("Ожидание добавления товара в корзину"):
            add_multiple_items.count_two()
        with allure.step("Открываем корзину"):
            add_multiple_items.sale_basket_click()
        with allure.step("Проверяем, что в корзине два товара"):
            assert add_multiple_items.get_text_count_products_basket() == COUNT_PRODUCTS
