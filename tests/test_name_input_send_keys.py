import pytest

from locators.main_page_locators import popup_back_call
from pages.anrex_main_page import MainPage
from tests.data import CALLBACK_TITLE


class TestNameInputSendKeys:

    def test_negative_name_input_send_keys(self, browser):
        name_input_send_keys = MainPage(browser)
        name_input_send_keys.open()
        name_input_send_keys.click_callback_link()
        name_input_send_keys.name_input_send_keys()
        input_element = name_input_send_keys.name_input_send_keys_error()
        class_attribute = input_element.get_attribute('class')
        # Проверка наличия класса 'has-error'
        assert 'input-field has-error' in class_attribute

    @pytest.mark.parametrize('name', [
        MainPage.generate_name(2, 'russian_letters'),
        MainPage.generate_name(49, 'russian_letters'),
        MainPage.generate_name(50, 'russian_letters'),
        MainPage.generate_name(51, 'russian_letters'),
        MainPage.generate_name(10, 'letters'),
    ])
    def test_positive_name_input_send_keys(self, browser, name):
        name_input_send_keys = MainPage(browser)
        name_input_send_keys.open()
        name_input_send_keys.click_callback_link()
        name_input_send_keys.t_name_input_send_keys(name)
        name_input_send_keys.phone_input_send_keys()
        name_input_send_keys.click_submit_application_button()
        name_input_send_keys.wait(popup_back_call)
        actual_title_text = name_input_send_keys.get_callback_title()
        assert CALLBACK_TITLE == actual_title_text

    def test_name_field_rejects_spaces(self, browser):
        name_input_send_keys = MainPage(browser)
        name_input_send_keys.open()
        name_input_send_keys.click_callback_link()
        # Получаем текущее значение поля "Ваше имя"
        name_input = name_input_send_keys.get_callback_popup_name_input()
        current_value = name_input.get_attribute("value")
        # Вводим пробел в поле "Ваше имя"
        name_input_send_keys.name_input_send_keys_spaces()
        # Проверяем, что значение поля не изменилось после ввода пробела
        assert name_input.get_attribute("value") == current_value

