import allure

from pages.basket_page import BasketPage
from tests_basket_page.data import TITLE_BASKET
from tests_main_page.urls import URL, BASKET


class TestDisplayCartTitle:

    @allure.title('В корзине отображается тайтл "Ваша корзина"')
    def test_display_cart_title(self, browser):
        display_cart_title = BasketPage(browser)
        with allure.step('Открываем страницу с корзиной'):
            display_cart_title.open(f'{URL}{BASKET}')
        with allure.step('Сохраняем заголовок'):
            title = display_cart_title.get_text_title_basket()
        with allure.step('Проверяем текст заголовка'):
            assert title == TITLE_BASKET