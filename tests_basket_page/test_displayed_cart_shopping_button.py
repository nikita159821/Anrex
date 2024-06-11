import allure

from pages.basket_page import BasketPage
from tests_main_page.urls import URL, BASKET


class TestDisplayedCartShoppingButton:

    @allure.title('В корзине отображается кнопка "Начать покупки"')
    def test_displayed_cart_shopping_button(self,browser):
        displayed_cart_shopping_button = BasketPage(browser)
        with allure.step('Открываем страницу с корзиной'):
            displayed_cart_shopping_button.open(f'{URL}{BASKET}')
        with allure.step('Проверяем, что отображается кнопка "Начать покупки"'):
            assert displayed_cart_shopping_button.get_button_shopping().is_displayed()