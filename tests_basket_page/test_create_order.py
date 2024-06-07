import time
import allure
import pytest

from pages.basket_page import BasketPage
from tests_basket_page.data import ORDER_CONFIRMATION, REQUIRED_CITY_FIELD, REQUIRED_STREET_FIELD, REQUIRED_HOUSE_FIELD, \
    REQUIRED_NAME_FIELD, REQUIRED_PHONE_FIELD
from tests_basket_page.test_data import TestData


class TestCreateOrder:

    @pytest.mark.parametrize('name, city, street, house, body, flat, phone, mail, comment',
                             (TestData.generate_test_create_oder()))
    @allure.title('Оформление заказа. Все поля заполнены')
    def test_positive_create_orders(self, browser, name, city, street, house, body, flat, phone, mail,
                                    comment):
        create_orders = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            create_orders.open_basket()
        with allure.step('Заполняем поля перед оформлением заказа'):
            create_orders.fill_form(name, city, street, house, body, flat, phone, mail, comment)
            time.sleep(6)
        with allure.step('Нажимаем "Оформить заказ"'):
            create_orders.click_button_arrange_order()
        with allure.step('Ожидаем оформление заказа'):
            create_orders.wait_for_order_confirmation()
            assert create_orders.get_text_order_confirmation() == ORDER_CONFIRMATION

    @pytest.mark.parametrize('test_data, expected_errors',
                             [(data, {'city': REQUIRED_CITY_FIELD, 'street': REQUIRED_STREET_FIELD,
                                      'house': REQUIRED_HOUSE_FIELD})
                              for data in TestData.generate_test_create_oder()] +
                             [(data, {'name': REQUIRED_NAME_FIELD, 'city': REQUIRED_CITY_FIELD,
                                      'house': REQUIRED_HOUSE_FIELD})
                              for data in TestData.generate_test_create_oder()] +
                             [(data, {'name': REQUIRED_NAME_FIELD, 'street': REQUIRED_STREET_FIELD,
                                      'phone': REQUIRED_PHONE_FIELD})
                              for data in TestData.generate_test_create_oder()])
    @allure.title('Оформление заказа. Проверка ошибок при незаполненных обязательных полях')
    def test_negative_create_orders_with_missing_fields(self, browser, test_data, expected_errors):
        name, city, street, house, flat, body, phone, mail, comment = test_data
        negative_create_orders = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            negative_create_orders.open_basket()
        with allure.step('Заполняем поля перед оформлением заказа'):
            form_data = {
                'name': name,
                'city': city,
                'street': street,
                'house': house,
                'flat': flat,
                'body': body,
                'phone': phone,
                'mail': mail,
                'comment': comment
            }
            for field, value in form_data.items():
                if field not in expected_errors:
                    negative_create_orders.fill_form(**{field: value})
        with allure.step('Нажимаем "Оформить заказ"'):
            negative_create_orders.click_button_arrange_order()
        with allure.step('Проверяем ошибку у каждого незаполненного поля'):
            for field, expected_error in expected_errors.items():
                error_text = getattr(negative_create_orders, f'get_text_error_{field}')()
                assert expected_error in error_text



