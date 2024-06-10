import allure

from pages.basket_page import BasketPage


class TestDisplayDeleteButton:

    @allure.title('Проверка отображение кнопки "Удалить" в корзине')
    def test_display_delete_button_for_item_in_cart(self, browser):
        display_delete_button = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            display_delete_button.open_basket()
        with allure.step('Проверяем, что в корзине отображается кнопка "Удалить"'):
            assert display_delete_button.get_remove_product_button().is_displayed()
