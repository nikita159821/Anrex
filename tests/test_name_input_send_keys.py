import time

from locators.main_page_locators import name_error
from pages.anrex_main_page import MainPage


class TestNameInputSendKeys:

    def test_name_input_send_keys(self, browser):
        name_input_send_keys = MainPage(browser)
        name_input_send_keys.open()
        name_input_send_keys.click_callback_link()
        name_input_send_keys.name_input_send_keys()
        input_element = name_input_send_keys.name_input_send_keys_error()
        class_attribute = input_element.get_attribute('class')
        # Проверка наличия класса 'has-error'
        assert 'input-field has-error' in class_attribute



