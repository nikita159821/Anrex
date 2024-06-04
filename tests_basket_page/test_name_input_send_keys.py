import allure
import pytest
from pages.basket_page import BasketPage
from tests_basket_page.data import BASKET_NAME, ORDER_CONFIRMATION, BASKET_RANDOM_NAME_NEGATIVE, ERROR_INPUTS_BASKET, \
    BASKET_RANDOM_NAME


class TestNameInputSendKeys:

    @pytest.mark.parametrize('name', BASKET_NAME + BASKET_RANDOM_NAME)
    @allure.title(
        'В корзине, вводим в поле "Ваше имя" буквы на кириллице, на латинице, с тире, без отчества, 2 буквы,49 букв,'
        '50 букв, 51 букву, 49 букв 51 букву')
    def test_positive_name_input_send_keys(self, browser, name):
        name_input_send_keys = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            name_input_send_keys.open_basket()
        with allure.step('Заполняем поле "Ваше имя" данными'):
            name_input_send_keys.name_input_send_keys(name)
        with allure.step('Заполняем остальные поля'):
            name_input_send_keys.fill_fields()
        with allure.step('Нажимаем "Оформить заказ"'):
            name_input_send_keys.click_button_arrange_order()
        with allure.step('Ожидаем оформление заказа'):
            name_input_send_keys.wait_for_order_confirmation()
            assert name_input_send_keys.get_text_order_confirmation() == ORDER_CONFIRMATION

    @pytest.mark.parametrize('name', BASKET_RANDOM_NAME_NEGATIVE)
    def test_negative_name_input_send_keys(self, browser, name):
        negative_name_input_send_keys = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            negative_name_input_send_keys.open_basket()
        with allure.step('Заполняем поле "Ваше имя" данными'):
            negative_name_input_send_keys.name_input_send_keys(name)
        with allure.step('Нажимаем "Оформить заказ"'):
            negative_name_input_send_keys.click_button_arrange_order()
        with allure.step('Ожидаем появления ошибки'):
            negative_name_input_send_keys.wait_for_error_name()
        with allure.step('Проверяем ошибку "Поле заполнено неверно" у поля "Ваше имя"'):
            assert negative_name_input_send_keys.get_text_error_name() == ERROR_INPUTS_BASKET


