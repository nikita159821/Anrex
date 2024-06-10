import allure

from pages.basket_page import BasketPage


class TestPlusButton:

    @allure.title('В корзине отображается кнопка "+" для добавления товара')
    def test_display_plus_button_in_basket(self, browser):
        plus_button_in_basket = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            plus_button_in_basket.open_basket()
        with allure.step('Проверяем, что в корзине отображается кнопка добавления товара "+"'):
            assert plus_button_in_basket.get_plus_button().is_displayed()
