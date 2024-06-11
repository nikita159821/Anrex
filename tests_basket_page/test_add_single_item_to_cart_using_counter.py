import allure
from pages.basket_page import BasketPage


class TestAddSingleItem:
    def test_add_single_item_to_cart_using_counter(self, browser):
        add_single_item_to_cart = BasketPage(browser)
        with allure.step('Открываем страницу каталога, добавляем товар в корзину и переходи в неё'):
            add_single_item_to_cart.open_basket()
        with allure.step('Добавляем второй товар через "+"'):
            add_single_item_to_cart.click_plus_button()
        with allure.step('Проверяем, что в корзине два товара'):
            assert add_single_item_to_cart.get_text_input_count_basket() == '2'
