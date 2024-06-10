import time

import allure
import pytest
from locators.basket_page_locators import input_mail_send_keys
from pages.basket_page import BasketPage
from tests_basket_page.data import ORDER_CONFIRMATION, EMAIL, EXPECTED_EMAIL, BASKET_EMAIL_NEGATIVE, ERROR_INPUT_EMAIl
from tests_basket_page.test_data import TestData


class TestEmailInputSendKeys:

    @pytest.mark.parametrize('name, city, street, house, body, flat, phone, mail, comment',
                             TestData.generate_test_email())
    def test_positive_email_input_send_keys(self, browser, name, city, street, house, body, flat, phone, mail,
                                            comment):
        email_input_send_keys = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            email_input_send_keys.open_basket()
        with allure.step('Заполняем поля перед оформлением заказа'):
            email_input_send_keys.fill_form(name=name, city=city, street=street, house=house, body=body, flat=flat, phone=phone, mail=mail, comment=comment)
        with allure.step('Нажимаем "Оформить заказ"'):
            email_input_send_keys.click_button_arrange_order()
        with allure.step('Ожидаем оформление заказа'):
            email_input_send_keys.wait_for_order_confirmation()
            assert email_input_send_keys.get_text_order_confirmation() == ORDER_CONFIRMATION

    def test_input_send_keys_email_whitespace(self, browser):
        input_send_keys_email_whitespace = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            input_send_keys_email_whitespace.open_basket()
        with allure.step('Заполняем поле E-mail'):
            input_send_keys_email_whitespace.mail_send_keys(EMAIL)
        with allure.step('Сохраняем итоговое значение из поля'):
            email = input_send_keys_email_whitespace.get_attribute_of_element(input_mail_send_keys, 'value')
        with allure.step('Сравниваем значение из поля с ожидаемым - EMAIL'):
            assert email == EXPECTED_EMAIL

    @pytest.mark.parametrize('email', BASKET_EMAIL_NEGATIVE)
    @allure.title('Ввод почты без доменной части, ввод почты без @, ввод почты с точками в имени аккаунта')
    def test_negative_email_input_send_keys(self, browser, email):
        negative_email_input_send_keys = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            negative_email_input_send_keys.open_basket()
        with allure.step('Заполняем поле E-mail'):
            negative_email_input_send_keys.mail_send_keys(email)
        with allure.step('Нажимаем "Оформить заказ"'):
            negative_email_input_send_keys.click_button_arrange_order()
        with allure.step('Ожидаем появления ошибки'):
            negative_email_input_send_keys.wait_for_error_email()
        with allure.step('Проверяем ошибку "Введен неверный e-mail" у поля "E-mail"'):
            assert negative_email_input_send_keys.get_text_error_email() == ERROR_INPUT_EMAIl
