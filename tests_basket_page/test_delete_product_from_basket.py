import time

import allure
from pages.basket_page import BasketPage


class TestDeleteProductFromBasket:

    @allure.title('Удаление единицы товара через счетчик в корзине')
    def test_delete_product_from_basket(self, browser):
        delete_product = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            delete_product.open_basket()
        with allure.step('Увеличиваем кол-во товара в корзине до 2'):
            delete_product.click_plus_button()
        with allure.step('Уменьшаем кол-во товара в корзине до 1'):
            delete_product.click_decrease_item_quantity()
        with allure.step('Проверяем, что товар удален из корзины'):
            assert delete_product.get_text_input_count_basket() == '1'
