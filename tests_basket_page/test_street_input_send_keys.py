import time

import allure
import pytest

from pages.basket_page import BasketPage
from tests_basket_page.data import ORDER_CONFIRMATION, STREET, ERROR_INPUT_STREET
from tests_basket_page.test_data import TestData


class TestStreetInputSendKeys:

    @pytest.mark.parametrize('name, city, street, house, body, flat, phone, mail, comment',
                             TestData.generate_test_street())
    def test_positive_street_input_send_keys(self, browser, name, city, street, house, body, flat, phone, mail,
                                             comment):
        street_input_send_keys = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            street_input_send_keys.open_basket()
        with allure.step('Заполняем поля перед оформлением заказа'):
            street_input_send_keys.fill_form(name=name, city=city, street=street, house=house, body=body, flat=flat, phone=phone, mail=mail, comment=comment)
        with allure.step('Нажимаем "Оформить заказ"'):
            street_input_send_keys.click_button_arrange_order()
        with allure.step('Ожидаем оформление заказа'):
            street_input_send_keys.wait_for_order_confirmation()
            assert street_input_send_keys.get_text_order_confirmation() == ORDER_CONFIRMATION

    def test_negative_street_input_send_keys(self, browser):
        street_input_send_keys = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            street_input_send_keys.open_basket()
        with allure.step('Вводим в поле "Улица" 2 символа"'):
            street_input_send_keys.street_send_keys(STREET)
        with allure.step('Нажимаем "Оформить заказ"'):
            street_input_send_keys.click_button_arrange_order()
        with allure.step('Ожидаем ошибку возле поля "Город доставки"'):
            street_input_send_keys.wait_for_error_street()
        with allure.step('Проверяем и сравниваем текст ошибки с ожидаемым'):
            assert street_input_send_keys.get_text_error_street() == ERROR_INPUT_STREET
