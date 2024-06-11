import allure
import pytest

from pages.basket_page import BasketPage
from tests_basket_page.data import PAYMENT_CASH, PAYMENT_BANK_CARD, PAYMENT_INSTALLMENT, PAYMENT_YANDEX_SPLIT


class TestDisplayPaymentMethods:
    payment_methods = [
        (PAYMENT_CASH, 'payment_in_cash', 'get_text_payment_in_cash'),
        (PAYMENT_BANK_CARD, 'payment_bank_card', 'get_text_payment_bank_card'),
        (PAYMENT_INSTALLMENT, 'payment_installment', 'get_text_payment_installment'),
        (PAYMENT_YANDEX_SPLIT, 'payment_yandex_split', 'get_text_payment_yandex_split')
    ]

    @pytest.mark.parametrize('expected_text, locator_name, method_name', payment_methods)
    @allure.title('В корзине отображается ожидаемый способ оплаты')
    def test_display_payment_methods(self, browser, expected_text, locator_name, method_name):
        display_payment = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            display_payment.open_basket()
        with allure.step(f'Проверяем отображение способа оплаты "{expected_text}"'):
            assert getattr(display_payment, method_name)() == expected_text
