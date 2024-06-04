import allure
import pytest
from pages.basket_page import BasketPage
from tests_basket_page.data import ORDER_CONFIRMATION, BASKET_CITY, ERROR_INPUT_CITY
from tests_basket_page.test_data import TestData


class TestCityInputSendKeys:

    @pytest.mark.parametrize('name, city, street, house, body, flat, phone, mail, comment',
                             TestData.generate_test_city())
    @allure.title(
        'В корзине, вводим в поле "Город доставки" валидные данные, 2 символа, 49 символов, 50 символов, 51 символ, Буквы со спец. символами')
    def test_positive_city_input_send_keys(self, browser, name, city, street, house, body, flat, phone, mail, comment):
        city_input_send_keys = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            city_input_send_keys.open_basket()
        with allure.step('Заполняем поля перед оформлением заказа'):
            city_input_send_keys.fill_form(name, city, street, house, body, flat, phone, mail, comment)
        with allure.step('Нажимаем "Оформить заказ"'):
            city_input_send_keys.click_button_arrange_order()
        with allure.step('Ожидаем оформление заказа'):
            city_input_send_keys.wait_for_order_confirmation()
            assert city_input_send_keys.get_text_order_confirmation() == ORDER_CONFIRMATION

    def test_negative_city_input_send_keys(self, browser):
        negative_city_input_send_keys = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            negative_city_input_send_keys.open_basket()
        with allure.step('Вводим в поле "Город доставки" 1 символ"'):
            negative_city_input_send_keys.delivery_city_send_keys(BASKET_CITY)
        with allure.step('Нажимаем "Оформить заказ"'):
            negative_city_input_send_keys.click_button_arrange_order()
        with allure.step('Ожидаем ошибку возле поля "Город доставки"'):
            negative_city_input_send_keys.wait_for_error_city()
        with allure.step('Проверяем и сравниваем текст ошибки с ожидаемым'):
            assert negative_city_input_send_keys.get_text_error_city() == ERROR_INPUT_CITY
