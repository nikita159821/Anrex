import allure
import pytest

from locators.main_page_locators import phone_error
from pages.anrex_main_page import MainPage


class TestPhoneInputSendKeys:

    @allure.title('В форме "Обратной сявзи" в поле "Ваш телефон" вводим 11 цифр')
    # Тест на ввод 11 цифр
    def test_positive_phone_input_form_feedback_send_keys(self, browser):
        phone_input_form_feedback_send_keys = MainPage(browser)
        phone_input_form_feedback_send_keys.open()
        phone_input_form_feedback_send_keys.get_section_footer()
        phone_input_form_feedback_send_keys.click_button_write()
        # Вводим цифры в поле "Ваш телефон"
        phone_input_form_feedback_send_keys.send_keys_input_phone_form_feedback()
        # Получаем текущее значение поля "Ваш телефон"
        phone_input = phone_input_form_feedback_send_keys.get_form_feedback_phone_input()
        current_value = phone_input.get_attribute("value")
        assert phone_input.get_attribute("value") == current_value

    @allure.title('В форме "Обратной сявзи" в поле "Ваш телефон" удаляем введенные значения')
    def test_phone_input_form_feedback_delete_send_keys(self, browser):
        phone_input_delete = MainPage(browser)
        phone_input_delete.open()
        phone_input_delete.get_section_footer()
        phone_input_delete.click_button_write()
        # Вводим цифры в поле "Ваш телефон"
        phone_input_delete.send_keys_input_phone_form_feedback()
        # Получаем текущее значение поля "Ваш телефон"
        phone_input = phone_input_delete.get_form_feedback_phone_input()
        # Удаляем введнный номер
        phone_input_delete.phone_input_delete_form_feedback()
        # Проверяем, что значение поля изменилось после удаления данных
        assert phone_input.get_attribute("value") == ''

    @allure.title('В форме "Обратной сявзи" в поле "Ваш телефон" вводим 12 цифр')
    def test_negative_phone_form_feedback_input_send_keys(self, browser):
        phone_input_send_keys = MainPage(browser)
        phone_input_send_keys.open()
        phone_input_send_keys.get_section_footer()
        phone_input_send_keys.click_button_write()
        # Вводим цифры в поле "Ваш телефон"
        phone_input_send_keys.send_keys_12_digits_form_feedback_phone_input()
        # Получаем текущее значение поля "Ваш телефон"
        phone_input = phone_input_send_keys.get_form_feedback_phone_input()
        current_value = phone_input.get_attribute("value")
        assert phone_input.get_attribute("value") == current_value

    # Вводим в поле "Ваш телефон" 1 цифру, буквы, спец. символы, пробел.
    @pytest.mark.parametrize('phone', [
        MainPage.generate_random_string(1, 'digits'),
        MainPage.generate_random_string(5, 'russian_letters'),
        MainPage.generate_random_string(5, 'punctuation'),
        ' '  # Добавляем пробел как один из параметров
    ])
    @allure.title('В форме "Обратной сявзи" в поле "Ваш телефон" вводим 1 цифру, буквы, спец. символы, пробел.')
    def test_negative_phone_form_feedback_input_send_keys(self, browser, phone):
        phone_form_feedback_input_send_keys = MainPage(browser)
        phone_form_feedback_input_send_keys.open()
        phone_form_feedback_input_send_keys.get_section_footer()
        phone_form_feedback_input_send_keys.click_button_write()
        phone_form_feedback_input_send_keys.form_phone_input_send_keys(phone)
        phone_form_feedback_input_send_keys.wait(phone_error)
        input_element = phone_form_feedback_input_send_keys.phone_input_send_keys_error()
        class_attribute = input_element.get_attribute('class')
        # Проверка наличия класса 'has-error'
        assert 'input-field has-error' in class_attribute
