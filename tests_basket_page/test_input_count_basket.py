import allure
from pages.basket_page import BasketPage
from tests_basket_page.data import SEND_KEYS_INPUT_COUNT_BASKET


class TestInputCountBasket:

    def test_input_count_basket_0(self, browser):
        input_count_basket = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            input_count_basket.open_basket()
        with allure.step('Указываем значение 0 в инпут счетчика'):
            input_count_basket.send_keys_input_count_basket('0')
            input_count_basket.remove_focus_from_input_count()
            assert input_count_basket.get_text_input_count_basket() == '1'

    def test_input_count_basket_float(self, browser):
        input_count_basket = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            input_count_basket.open_basket()
        with allure.step('Указываем значение 2.5 в инпут счетчика'):
            input_count_basket.send_keys_input_count_basket('2.5')
            input_count_basket.remove_focus_from_input_count()
            assert input_count_basket.get_text_input_count_basket() == '2'

    def test_input_count_basket(self, browser):
        input_count_basket = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            input_count_basket.open_basket()
        with allure.step('Указываем значение в инпут счетчика'):
            input_count_basket.send_keys_input_count_basket(SEND_KEYS_INPUT_COUNT_BASKET)
            input_count_basket.remove_focus_from_input_count()
            assert input_count_basket.get_text_input_count_basket() == '3'
