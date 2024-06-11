import allure

from pages.basket_page import BasketPage
from tests_basket_page.data import TEXT_BASKET
from tests_main_page.urls import URL, BASKET


class TestDisplayCartText:

    @allure.title('В корзине отображается текст "Вы еще не добавили ни одного товара в Вашу корзину"')
    def test_display_cart_text(self, browser):
        display_cart_text = BasketPage(browser)
        with allure.step('Открываем страницу с корзиной'):
            display_cart_text.open(f'{URL}{BASKET}')
        with allure.step('Проверяем, что в корзине отображается текст "Вы еще не добавили ни одного товара в Вашу корзину"'):
            assert display_cart_text.get_text_basket() == TEXT_BASKET
