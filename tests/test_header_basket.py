from locators.main_page_locators import basket_count
from pages.anrex_main_page import MainPage
from tests.urls import URL, BASKET


class TestHeaderBasket:

    # Проверка, что отображается иконка корзины в шапке сайта
    def test_header_displays_basket(self, browser):
        displays_basket = MainPage(browser)
        displays_basket.open()
        basket = displays_basket.get_sale_basket()
        assert basket.is_displayed()

    # Проверка перехода в корзину через иконку на главной странице
    def test_header_basket_redirect(self, browser):
        displays_basket = MainPage(browser)
        displays_basket.open()
        displays_basket.sale_basket_click()
        basket_url = displays_basket.get_current_url()
        assert basket_url == f'{URL}{BASKET}'

    # Проверка, что при добавлении товара в корзину
    # возле иконки появляется кол-во товаров
    def test_basket_count_displayed_after_adding_product(self,browser):
        count_displayed = MainPage(browser)
        count_displayed.open_catalog()
        count_displayed.button_click_cards()
        count_displayed.wait_for_element_text_to_be(basket_count)
        basket_count_value = count_displayed.basket_count()
        assert basket_count_value == '(1)'
