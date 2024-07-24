import allure
import pytest

from locators.basket_page_locators import input_body_send_keys
from pages.basket_page import BasketPage
from tests_basket_page.data import ORDER_CONFIRMATION, BODY
from tests_basket_page.test_data import TestData


class TestBodyInputSendKeys:

    @pytest.mark.parametrize('name, city, street, house, body, flat, phone, mail, comment',
                             TestData.generate_test_body())
    def test_positive_body_input_send_keys(self, browser, name, city, street, house, body, flat, phone, mail,
                                           comment):
        body_input_send_keys = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            body_input_send_keys.open_basket()
        with allure.step('Заполняем поля перед оформлением заказа'):
            body_input_send_keys.fill_form(name=name, city=city, street=street, house=house, body=body, flat=flat, phone=phone, mail=mail, comment=comment)
        with allure.step('Нажимаем "Оформить заказ"'):
            body_input_send_keys.click_button_arrange_order()
        with allure.step('Ожидаем оформление заказа'):
            body_input_send_keys.wait_for_order_confirmation()
            assert body_input_send_keys.get_text_order_confirmation() == ORDER_CONFIRMATION

    def test_input_send_keys_six_numbers(self, browser):
        body_input_send_keys = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            body_input_send_keys.open_basket()
        with allure.step('Заполняем поле корпус'):
            body_input_send_keys.body_send_keys('123456')
        with allure.step('Сохраняем итоговое значение из поля'):
            body = body_input_send_keys.get_attribute_of_element(input_body_send_keys, 'value')
        with allure.step('Сравниваем значение из поля с ожидаемым - 12345'):
            assert body == BODY
