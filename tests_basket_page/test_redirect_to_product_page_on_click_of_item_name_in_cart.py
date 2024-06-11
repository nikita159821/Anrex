import allure

from pages.basket_page import BasketPage


class TestRedirectProductPageOnClick:
    def test_redirect_to_product_page_on_click_of_item_name_in_cart(self, browser):
        redirect_to_product_page = BasketPage(browser)
        with allure.step('Открываем страницу каталога, добавляем товар в корзину и переходи в неё'):
            redirect_to_product_page.open_basket()
        with allure.step('Сохраняем url товара в корзине'):
            card_url = redirect_to_product_page.get_url_products_basket()
        with allure.step('Нажимаем на название товара в корзине'):
            redirect_to_product_page.click_name_card_basket()
        with allure.step('Получаем url открытой страницы. Сравниваем с сохранным в корзине'):
            assert redirect_to_product_page.get_current_url() == card_url
