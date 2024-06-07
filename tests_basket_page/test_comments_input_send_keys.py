import allure
import pytest

from locators.basket_page_locators import input_your_comment_send_keys
from pages.basket_page import BasketPage
from tests_basket_page.data import ORDER_CONFIRMATION, NEW_COMMENTS
from tests_basket_page.test_data import TestData


class TestCommentsInputSendKeys:

    @pytest.mark.parametrize('name, city, street, house, body, flat, phone, mail, comment',
                             TestData.generate_test_comment())
    @allure.title('Вводим в поле "Комментарий" - буквы, цифры, спец.символы,на латинице,3999 символов,4000 символов')
    def test_positive_comments_input_send_keys(self, browser, name, city,
                                               street, house, body, flat,
                                               phone, mail, comment):
        comments_input_send_keys = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            comments_input_send_keys.open_basket()
        with allure.step('Заполняем поля перед оформлением заказа'):
            comments_input_send_keys.fill_form(name=name, city=city, street=street, house=house, body=body, flat=flat, phone=phone, mail=mail, comment=comment)
        with allure.step('Нажимаем "Оформить заказ"'):
            comments_input_send_keys.click_button_arrange_order()
        with allure.step('Ожидаем оформление заказа'):
            comments_input_send_keys.wait_for_order_confirmation()
            assert comments_input_send_keys.get_text_order_confirmation() == ORDER_CONFIRMATION

    @allure.title('Вводим в поле "Комментарий" - 4001 символов')
    def test_negative_comments_input_send_keys(self, browser):
        negative_comments_input_send_keys = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            negative_comments_input_send_keys.open_basket()
        with allure.step('Заполняем поле комментарий'):
            negative_comments_input_send_keys.your_comment_send_keys(NEW_COMMENTS)
        with allure.step('Сохраняем итоговое значение из поля'):
            comment = negative_comments_input_send_keys.get_attribute_of_element(input_your_comment_send_keys, 'value')
        with allure.step('Проверяем, что длина сохраненного комментария равна 4000 символов'):
            assert len(comment) == 4000

