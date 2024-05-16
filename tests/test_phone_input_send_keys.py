import pytest

from locators.main_page_locators import input_phone
from pages.anrex_main_page import MainPage


class TestPhoneInputSendKeys:

    # Тест на ввод 11 цифр
    def test_positive_phone_input_send_keys(self, browser):
        phone_input_send_keys = MainPage(browser)
        phone_input_send_keys.open()
        phone_input_send_keys.click_callback_link()
        # Вводим цифры в поле "Ваш телефон"
        phone_input_send_keys.phone_input_send_keys()
        # Получаем текущее значение поля "Ваш телефон"
        phone_input = phone_input_send_keys.get_callback_popup_phone_input()
        current_value = phone_input.get_attribute("value")
        assert phone_input.get_attribute("value") == current_value

    # Тест на удаление цифр
    def test_phone_input_delete_send_keys(self, browser):
        phone_input_delete = MainPage(browser)
        phone_input_delete.open()
        phone_input_delete.click_callback_link()
        phone_input_delete.phone_input_send_keys()
        # Получаем текущее значение поля "Ваш телефон"
        phone_input = phone_input_delete.get_callback_popup_phone_input()
        # Удаляем введнный номер
        phone_input_delete.phone_input_delete()
        # Проверяем, что значение поля изменилось после удаления данных
        assert phone_input.get_attribute("value") == ''

    # Тест на ввод 12 цифр
    def test_negative_phone_input_send_keys(self, browser):
        phone_input_send_keys = MainPage(browser)
        phone_input_send_keys.open()
        phone_input_send_keys.click_callback_link()
        # Вводим цифры в поле "Ваш телефон"
        phone_input_send_keys.send_keys_12_digits_to_phone_input()
        # Получаем текущее значение поля "Ваш телефон"
        phone_input = phone_input_send_keys.get_callback_popup_phone_input()
        current_value = phone_input.get_attribute("value")
        assert phone_input.get_attribute("value") == current_value

    # Вводим в поле "Ваш телефон 1 цифру, буквы, спец. символы, пробел.
    @pytest.mark.parametrize('phone', [
        MainPage.generate_random_string(1, 'digits'),
        MainPage.generate_random_string(5, 'russian_letters'),
        MainPage.generate_random_string(5, 'punctuation'),
        ' '  # Добавляем пробел как один из параметров
    ])
    def test_negative_phone_input_send_keys(self, browser, phone):
        phone_input_send_keys = MainPage(browser)
        phone_input_send_keys.open()
        phone_input_send_keys.click_callback_link()
        phone_input_send_keys.t_phone_input_send_keys(phone, input_phone)
        input_element = phone_input_send_keys.phone_input_send_keys_error()
        class_attribute = input_element.get_attribute('class')
        # Проверка наличия класса 'has-error'
        assert 'input-field has-error' in class_attribute
