import allure

from pages.basket_page import BasketPage
from tests_basket_page.data import BREADCRUMB_HOME_TEXT, BREADCRUMB_BASKET_TEXT


class TestBreadcrumbsInBasket:
    def test_breadcrumb_home_in_basket(self, browser):
        breadcrumb_home = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            breadcrumb_home.open_basket()
        with allure.step('Проверяем, что на странице корзины отображается хлебная крошка "Главная"'):
            assert breadcrumb_home.get_text_home_breadcrumb() == BREADCRUMB_HOME_TEXT

    def test_breadcrumb_basket_in_basket(self, browser):
        breadcrumb_basket = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            breadcrumb_basket.open_basket()
        with allure.step('Проверяем, что на странице корзины отображается хлебная крошка "Корзина"'):
            assert breadcrumb_basket.get_text_basket_breadcrumb() == BREADCRUMB_BASKET_TEXT

