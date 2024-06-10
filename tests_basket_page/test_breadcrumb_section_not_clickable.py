import allure

from pages.basket_page import BasketPage
from tests_main_page.urls import BASKET, URL


class TestBreadcrumbSectionNotClickable:
    @allure.title("Проверка, что открытый раздел в хлебных крошках не является кликабельным")
    def test_breadcrumb_section_not_clickable(self, browser):
        breadcrumb = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            breadcrumb.open_basket()
        with allure.step('Нажимает на текст хлебной крошки "Корзина"'):
            breadcrumb.click_basket_breadcrumb()
        with allure.step('Проверяем, что после нажатия остались в корзине"'):
            assert breadcrumb.get_current_url() == f'{URL}{BASKET}'
