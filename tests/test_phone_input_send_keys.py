import allure
import pytest

from locators.main_page_locators import input_phone, phone_error, callback_link
from pages.anrex_main_page import MainPage
from tests.data import PHONE_FORM, HAS_ERROR_PHONE


class TestPhoneInputSendKeys:

    @allure.title('В форме "Заявка на обратный звонок", в поле "Ваш телефон" вводим 11 цифр')
    def test_positive_phone_input_send_keys(self, browser):
        phone_input_send_keys = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            phone_input_send_keys.open()
        with allure.step('Нажимаем на "Заказать обратный звонок"'):
            phone_input_send_keys.click_callback_link()
        with allure.step('Вводим цифры в поле "Ваш телефон"'):
            phone_input_send_keys.phone_input_send_keys()
        with allure.step('Сравниваем полученное значение из поля и с ожидаемым'):
            assert phone_input_send_keys.get_callback_popup_phone_input().get_attribute("value") == PHONE_FORM

    @allure.title('В форме "Заявка на обратный звонок", в поле "Ваш телефон" удаляем введенные значения')
    def test_phone_input_delete_send_keys(self, browser):
        phone_input_delete = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            phone_input_delete.open()
        with allure.step('Нажимаем на "Заказать обратный звонок"'):
            phone_input_delete.click_callback_link()
        with allure.step('Вводим цифры в поле "Ваш телефон"'):
            phone_input_delete.phone_input_send_keys()
        with allure.step('Удаляем введенный номер'):
            phone_input_delete.phone_input_delete()
        with allure.step('Проверяем, что значение поля изменилось после удаления данных'):
            assert phone_input_delete.get_callback_popup_phone_input().get_attribute("value") == ''

    @allure.title('В форме "Заявка на обратный звонок", в поле "Ваш телефон" вводим 12 цифр')
    def test_negative_phone_input_send_keys_12_digits(self, browser):
        phone_input_send_keys = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            phone_input_send_keys.open()
        with allure.step('Нажимаем на "Заказать обратный звонок"'):
            phone_input_send_keys.click_callback_link()
        with allure.step('Вводим цифры в поле "Ваш телефон"'):
            phone_input_send_keys.send_keys_12_digits_to_phone_input()
        with allure.step('Сравниваем полученное значение из поля и с ожидаемым'):
            assert phone_input_send_keys.get_callback_popup_phone_input().get_attribute("value") == PHONE_FORM

    @pytest.mark.parametrize('phone', [
        MainPage.generate_random_string(1, 'digits'),
        MainPage.generate_random_string(5, 'russian_letters'),
        MainPage.generate_random_string(5, 'punctuation'),
        ' '  # Добавляем пробел как один из параметров
    ])
    @allure.title('В форме "Заявка на обратный звонок", в поле "Ваш телефон" вводим 1 цифру, буквы, спец. символы, '
                  'пробел.')
    def test_negative_phone_input_send_keys(self, browser, phone):
        phone_input_send_keys = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            phone_input_send_keys.open()
        with allure.step('Ожидаем пока загрузится страница'):
            phone_input_send_keys.wait(callback_link)
        with allure.step('Нажимаем на "Заказать обратный звонок"'):
            phone_input_send_keys.click_callback_link()
        with allure.step('Заполняем поле "Ваш телефон" данными'):
            phone_input_send_keys.t_phone_input_send_keys(phone, input_phone)
        with allure.step('Ожидаем пока поле "Ваше имя" будет подсвечиваться красным'):
            phone_input_send_keys.wait(phone_error)
        with allure.step('Проверка наличия класса "has-error"'):
            assert phone_input_send_keys.phone_input_send_keys_error() == HAS_ERROR_PHONE
