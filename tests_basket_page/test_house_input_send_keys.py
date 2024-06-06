import allure
import pytest

from pages.anrex_main_page import MainPage
from pages.basket_page import BasketPage
from tests_basket_page.data import ORDER_CONFIRMATION, ERROR_INPUT_HOUSE_digits, ERROR_INPUT_HOUSE_russian_letters, \
    ERROR_INPUT_HOUSE_whitespace
from tests_basket_page.test_data import TestData


class TestHouseInputSendKeys:

    @pytest.mark.parametrize('name, city, street, house, body, flat, phone, mail, comment',
                             TestData.generate_test_house())
    def test_positive_house_input_send_keys(self, browser, name, city, street, house, body, flat, phone, mail,
                                            comment):
        house_input_send_keys = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            house_input_send_keys.open_basket()
        with allure.step('Заполняем поля перед оформлением заказа'):
            house_input_send_keys.fill_form(name, city, street, house, body, flat, phone, mail, comment)
        with allure.step('Нажимаем "Оформить заказ"'):
            house_input_send_keys.click_button_arrange_order()
        with allure.step('Ожидаем оформление заказа'):
            house_input_send_keys.wait_for_order_confirmation()
            assert house_input_send_keys.get_text_order_confirmation() == ORDER_CONFIRMATION

    @pytest.mark.parametrize('house, expected_error', [
        (MainPage.generate_random_string(4, 'digits'), ERROR_INPUT_HOUSE_digits),
        (MainPage.generate_random_string(6, 'russian_letters'), ERROR_INPUT_HOUSE_russian_letters),
        (' ', ERROR_INPUT_HOUSE_whitespace)
    ])
    @allure.title('Вводим 4 символа, буквы, пробел.')
    def test_negative_house_input_send_keys(self, browser, house,expected_error):
        negative_house_input_send_keys = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            negative_house_input_send_keys.open_basket()
        with allure.step('Заполняем поле "Дом" данными'):
            negative_house_input_send_keys.house_send_keys(house)
        with allure.step('Нажимаем "Оформить заказ"'):
            negative_house_input_send_keys.click_button_arrange_order()
        with allure.step('Ожидаем появления ошибки'):
            negative_house_input_send_keys.wait_for_error_house()
        with allure.step('Проверяем ошибку "Поле заполнено неверно" у поля "Ваше имя"'):
            assert negative_house_input_send_keys.get_text_error_house() == expected_error
