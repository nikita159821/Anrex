import allure
import pytest

from locators.main_page_locators import phone_error, button_write, input_phone_form_feedback
from pages.anrex_main_page import MainPage
from tests_main_page.data import PHONE_FORM, HAS_ERROR_PHONE


class TestPhoneInputSendKeys:

    @allure.title('В форме "Обратной связи" в поле "Ваш телефон" вводим 11 цифр')
    def test_positive_phone_input_form_feedback_send_keys(self, browser):
        phone_input_form_feedback_send_keys = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            phone_input_form_feedback_send_keys.open()
        with allure.step('Скроллим до футера'):
            phone_input_form_feedback_send_keys.get_section_footer()
        with allure.step('Добавляем ожидание после скролла'):
            phone_input_form_feedback_send_keys.wait_for_element(button_write)
        with allure.step('Нажимаем кнопку "Написать нам"'):
            phone_input_form_feedback_send_keys.click_button_write()
        with allure.step('Добавляем ожидание'):
            phone_input_form_feedback_send_keys.wait_for_element(input_phone_form_feedback)
        with allure.step('Вводим цифры в поле "Ваш телефон"'):
            phone_input_form_feedback_send_keys.send_keys_input_phone_form_feedback()
        with allure.step('Находим поле "Ваш телефон"'):
            phone_input = phone_input_form_feedback_send_keys.get_form_feedback_phone_input()
        with allure.step('Получаем текущее значение поля "Ваш телефон"'):
            current_value = phone_input.get_attribute("value")
        with allure.step('Сравниваем значение поля "Ваш телефон" с ожидаемым'):
            assert phone_input.get_attribute("value") == current_value

    @allure.title('В форме "Обратной связи" в поле "Ваш телефон" удаляем введенные значения')
    def test_phone_input_form_feedback_delete_send_keys(self, browser):
        phone_input_delete = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            phone_input_delete.open()
        with allure.step('Скроллим до футера'):
            phone_input_delete.get_section_footer()
        with allure.step('Добавляем ожидание после скролла'):
            phone_input_delete.wait_for_element(button_write)
        with allure.step('Нажимаем кнопку "Написать нам"'):
            phone_input_delete.click_button_write()
        with allure.step('Добавляем ожидание'):
            phone_input_delete.wait_for_element(input_phone_form_feedback)
        with allure.step('Вводим цифры в поле "Ваш телефон"'):
            phone_input_delete.send_keys_input_phone_form_feedback()
        with allure.step('Возвращаем поле "Ваш телефон" и сохраняем его значение'):
            phone_input = phone_input_delete.get_form_feedback_phone_input()
        with allure.step('Удаляем введенный номер'):
            phone_input_delete.phone_input_delete_form_feedback()
        with allure.step('Проверяем, что значение поля изменилось после удаления данных'):
            assert phone_input.get_attribute("value") == ''

    @allure.title('В форме "Обратной связи" в поле "Ваш телефон" вводим 12 цифр')
    def test_negative_phone_form_feedback_input_send_keys_12_digits(self, browser):
        phone_input_send_keys = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            phone_input_send_keys.open()
        with allure.step('Скроллим до футера'):
            phone_input_send_keys.get_section_footer()
        with allure.step('Добавляем ожидание после скролла'):
            phone_input_send_keys.wait_for_element(button_write)
        with allure.step('Нажимаем кнопку "Написать нам"'):
            phone_input_send_keys.click_button_write()
        with allure.step('Добавляем ожидание'):
            phone_input_send_keys.wait_for_element(input_phone_form_feedback)
        with allure.step('Вводим цифры в поле "Ваш телефон"'):
            phone_input_send_keys.send_keys_12_digits_form_feedback_phone_input()
        with allure.step('Возвращаем поле "Ваш телефон" и сохраняем его значение'):
            phone_input = phone_input_send_keys.get_form_feedback_phone_input()
        with allure.step('Сравниваем значение поля "Ваш телефон" с ожидаемым'):
            assert phone_input.get_attribute("value") == PHONE_FORM

    # Вводим в поле "Ваш телефон" 1 цифру, буквы, спец. символы, пробел.
    @pytest.mark.parametrize('phone', [
        MainPage.generate_random_string(1, 'digits'),
        MainPage.generate_random_string(5, 'russian_letters'),
        MainPage.generate_random_string(5, 'punctuation'),
        ' '  # Добавляем пробел как один из параметров
    ])
    @allure.title('В форме "Обратной связи" в поле "Ваш телефон" вводим 1 цифру, буквы, спец. символы, пробел.')
    def test_negative_phone_form_feedback_input_send_keys(self, browser, phone):
        phone_form_feedback_input_send_keys = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            phone_form_feedback_input_send_keys.open()
        with allure.step('Скроллим до футера'):
            phone_form_feedback_input_send_keys.get_section_footer()
        with allure.step('Добавляем ожидание после скролла'):
            phone_form_feedback_input_send_keys.wait_for_element(button_write)
        with allure.step('Нажимаем кнопку "Написать нам"'):
            phone_form_feedback_input_send_keys.click_button_write()
        with allure.step('Добавляем ожидание'):
            phone_form_feedback_input_send_keys.wait_for_element(input_phone_form_feedback)
        with allure.step('Вводим цифры в поле "Ваш телефон"'):
            phone_form_feedback_input_send_keys.form_phone_input_send_keys(phone)
        with allure.step('Ожидание'):
            phone_form_feedback_input_send_keys.wait(phone_error)
        with allure.step('Проверка наличия класса "has-error"'):
            assert phone_form_feedback_input_send_keys.name_input_send_keys_error() == HAS_ERROR_PHONE

