import allure

from pages.basket_page import BasketPage


class TestDecreaseItemQuantity:
    @allure.title('В корзине отображается кнопка "-" для уменьшения кол-ва товара')
    def test_decrease_item_quantity_in_cart(self,browser):
        decrease_item_quantity = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            decrease_item_quantity.open_basket()
        with allure.step('Проверяем, что в корзине отображается кнопка уменьшения кол-ва товаров "-"'):
            assert decrease_item_quantity.get_decrease_item_quantity().is_displayed()
