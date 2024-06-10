import allure

from pages.basket_page import BasketPage
from tests_main_page.urls import URL


class TestBreadcrumbNavigationToHome:
    @allure.title("Проверка перехода на главную страницу через хлебные крошки")
    def test_breadcrumb_navigation_to_home(self, browser):
        breadcrumb = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            breadcrumb.open_basket()
        with allure.step('Нажимает на текст хлебной крошки "Главная"'):
            breadcrumb.click_home_breadcrumb()
        with allure.step('Проверяем, что открылась главная страница"'):
            assert breadcrumb.get_current_url() == f'{URL}'
