import allure
import pytest

from locators.main_page_locators import popup_back_call
from pages.anrex_main_page import MainPage
from tests.data import CALLBACK_TITLE


class TestNameInputSendKeys:

    @pytest.mark.parametrize('name', [
        MainPage.generate_random_string(2, 'russian_letters'),
        MainPage.generate_random_string(49, 'russian_letters'),
        MainPage.generate_random_string(50, 'russian_letters'),
        MainPage.generate_random_string(51, 'russian_letters'),
        MainPage.generate_random_string(10, 'letters'),
    ])
    @allure.title('В форме "Заявка на обратный звонок", вводим в поле "Ваше имя" 2 буквы, 49, букв, 50 букв, '
                  '51 букву, 10 букв на латинице')
    def test_positive_name_input_send_keys(self, browser, name):
        name_input_send_keys = MainPage(browser)
        name_input_send_keys.open()
        name_input_send_keys.click_callback_link()
        name_input_send_keys.t_name_input_send_keys(name)
        name_input_send_keys.phone_input_send_keys()
        name_input_send_keys.click_submit_application_button()
        name_input_send_keys.wait(popup_back_call)
        assert name_input_send_keys.get_callback_title() == CALLBACK_TITLE

    @allure.title('В форме "Заявка на обратный звонок", удаляем введенные данные из поля "Ваше имя"')
    def test_name_input_delete_send_keys(self, browser):
        name_input_delete = MainPage(browser)
        name_input_delete.open()
        name_input_delete.click_callback_link()
        name_input_delete.name_input_send_keys()
        # Удаляем введенный текст
        name_input_delete.name_input_delete()
        # Проверяем, что значение поля изменилось после удаления данных
        assert name_input_delete.get_callback_popup_name_input().get_attribute("value") == ''

    @pytest.mark.parametrize('name', [
        MainPage.generate_random_string(1, 'russian_letters'),
        MainPage.generate_random_string(1, 'digits'),
        MainPage.generate_random_string(5, 'punctuation'),
        ' '
    ])
    @allure.title('В форме "Заявка на обратный звонок", вводим в поле "Ваше имя" 1 букву, 1 цифру, 5 спец. символов, '
                  'пробел.')
    def test_negative_name_input_send_keys(self, browser, name):
        name_input_send_keys = MainPage(browser)
        name_input_send_keys.open()
        name_input_send_keys.click_callback_link()
        name_input_send_keys.t_name_input_send_keys(name)
        input_element = name_input_send_keys.name_input_send_keys_error()
        class_attribute = input_element.get_attribute('class')
        # Проверка наличия класса 'has-error'
        assert 'input-field has-error' in class_attribute
