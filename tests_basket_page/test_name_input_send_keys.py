import allure
import pytest
from pages.basket_page import BasketPage
from tests_basket_page.data import ORDER_CONFIRMATION, BASKET_RANDOM_NAME_NEGATIVE, ERROR_INPUTS_BASKET
from tests_basket_page.test_data import TestData


class TestNameInputSendKeys:

    @pytest.mark.parametrize('name, city, street, house, body, flat, phone, mail, comment',
                             TestData.generate_test_name())
    @allure.title(
        'В корзине, вводим в поле "Ваше имя" буквы на кириллице, на латинице, с тире, без отчества и в поле "Город доставки" валидные данные, в поле "Улица" валидные данные, в поле "Дом" валидные данные, в поле "Корпус" валидные данные, в поле "Квартира" валидные данные, в поле "Телефон" валидные данные, в поле "Email" валидные данные, в поле "Комментарий" валидные данные')
    def test_positive_name_input_send_keys(self, browser, name, city,
                                           street, house, body, flat,
                                           phone, mail, comment):
        name_input_send_keys = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            name_input_send_keys.open_basket()
        with allure.step('Заполняем поля перед оформлением заказа'):
            name_input_send_keys.fill_form(name=name, city=city, street=street, house=house, body=body, flat=flat,
                                           phone=phone, mail=mail, comment=comment)
        with allure.step('Нажимаем "Оформить заказ"'):
            name_input_send_keys.click_button_arrange_order()
        with allure.step('Ожидаем оформление заказа'):
            name_input_send_keys.wait_for_order_confirmation()
            assert name_input_send_keys.get_text_order_confirmation() == ORDER_CONFIRMATION

    @pytest.mark.parametrize('name', BASKET_RANDOM_NAME_NEGATIVE)
    @allure.title('Вводим спец. символы, буквы с цифрой, одну букву в имени.')
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
