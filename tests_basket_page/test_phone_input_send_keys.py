import allure
import pytest

from locators.basket_page_locators import input_phone_number_send_keys
from pages.basket_page import BasketPage
from tests_basket_page.data import ORDER_CONFIRMATION, BASKET_PHONE_NEGATIVE, ERROR_INPUT_PHONE_ONE_DIGIT, \
    BASKET_PHONE_LETTERS, BASKET_PHONE_TWELVE_DIGIT, PHONE_NUMBER, BASKET_PHONE_INPUT_MASK
from tests_basket_page.test_data import TestData


class TestPhoneInputSendKeys:

    @pytest.mark.parametrize('name, city, street, house, body, flat, phone, mail, comment',
                             TestData.generate_test_phone())
    @allure.title('Вводим в поле телефон 11 цифр')
    def test_send_keys_valid_phone(self, browser, name, city,
                                   street, house, body, flat,
                                   phone, mail, comment):
        send_keys_valid_phone = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            send_keys_valid_phone.open_basket()
        with allure.step('Заполняем поля перед оформлением заказа'):
            send_keys_valid_phone.fill_form(name=name, city=city, street=street, house=house, body=body, flat=flat, phone=phone, mail=mail, comment=comment)
        with allure.step('Нажимаем "Оформить заказ"'):
            send_keys_valid_phone.click_button_arrange_order()
        with allure.step('Ожидаем оформление заказа'):
            send_keys_valid_phone.wait_for_order_confirmation()
            assert send_keys_valid_phone.get_text_order_confirmation() == ORDER_CONFIRMATION

    @allure.title('Вводим в поле телефон одну цифру')
    def test_send_keys_one_digit_phone(self, browser):
        send_keys_one_digit_phone = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            send_keys_one_digit_phone.open_basket()
        with allure.step('Заполняем поле телефон'):
            send_keys_one_digit_phone.phone_number_send_keys(BASKET_PHONE_NEGATIVE)
        with allure.step('Нажимаем "Оформить заказ"'):
            send_keys_one_digit_phone.click_button_arrange_order()
        with allure.step('Ожидаем появления ошибки'):
            send_keys_one_digit_phone.wait_for_error_phone()
        with allure.step('Проверяем ошибку  у поля "Номер телефона"'):
            assert send_keys_one_digit_phone.get_text_error_phone() == ERROR_INPUT_PHONE_ONE_DIGIT

    @allure.title('Вводим в поле телефон 12 цифр')
    def test_send_keys_twelve_digit_phone(self, browser):
        send_keys_twelve_digit_phone = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            send_keys_twelve_digit_phone.open_basket()
        with allure.step('Заполняем поле телефон'):
            send_keys_twelve_digit_phone.phone_number_send_keys(BASKET_PHONE_TWELVE_DIGIT)
        with allure.step('Сохраняем итоговое значение из поля'):
            phone = send_keys_twelve_digit_phone.get_attribute_of_element(input_phone_number_send_keys, 'value')
        with allure.step('Сравниваем значение из поля с ожидаемым - PHONE_NUMBER'):
            assert phone == PHONE_NUMBER

    @allure.title('Вводим буквы в поле телефон')
    def test_send_keys_letters_phone(self, browser):
        send_keys_letters_phone = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            send_keys_letters_phone.open_basket()
        with allure.step('Заполняем поле телефон'):
            send_keys_letters_phone.phone_number_send_keys(BASKET_PHONE_LETTERS)
        with allure.step('Сохраняем итоговое значение из поля'):
            phone = send_keys_letters_phone.get_attribute_of_element(input_phone_number_send_keys, 'value')
        with allure.step('Сравниваем значение из поля с ожидаемым - пустая строка'):
            assert phone == ''

    @allure.title('При вводе номера телефона, появляется маска +7')
    def test_phone_number_input_mask(self, browser):
        phone_number_input_mask = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            phone_number_input_mask.open_basket()
        with allure.step('Заполняем поле телефон'):
            phone_number_input_mask.phone_number_send_keys(BASKET_PHONE_NEGATIVE)
        with allure.step('Сохраняем итоговое значение из поля'):
            phone = phone_number_input_mask.get_attribute_of_element(input_phone_number_send_keys, 'value')
        with allure.step('Сравниваем значение из поля с ожидаемым - +7'):
            assert phone.startswith(BASKET_PHONE_INPUT_MASK[0])

