import allure

from locators.main_page_locators import basket_count
from pages.anrex_main_page import MainPage
from tests_main_page.urls import URL, BASKET


class TestHeaderBasket:

    @allure.title('Проверка, что отображается иконка корзины в шапке сайта')
    def test_header_displays_basket(self, browser):
        displays_basket = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            displays_basket.open()
        with allure.step('Находим иконку корзины'):
            assert displays_basket.get_sale_basket().is_displayed()

    @allure.title('Проверка перехода в корзину через иконку на главной странице')
    def test_header_basket_redirect(self, browser):
        displays_basket = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            displays_basket.open()
        with allure.step('Нажимаем на иконку корзины в шапке сайта'):
            displays_basket.sale_basket_click()
        with allure.step('Проверяем что открылась страница корзины'):
            assert displays_basket.get_current_url() == f'{URL}{BASKET}'

    @allure.title('При добавлении товара в корзину,возле иконки появляется кол-во товаров')
    def test_basket_count_displayed_after_adding_product(self, browser):
        count_displayed = MainPage(browser)
        with allure.step('Открываем страницу каталога'):
            count_displayed.open_catalog()
            with allure.step('Нажимаем "Добавить в корзину" у карточки товара'):
                count_displayed.button_click_cards()
        with allure.step('Ждем пока товар добавится в корзину'):
            count_displayed.wait_for_element(basket_count)
        with allure.step('Проверяем, что в корзину добавился один товар'):
            assert count_displayed.basket_count() == '1'
