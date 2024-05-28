import allure
import pytest

from locators.main_page_locators import popup_back_call, name_error
from pages.anrex_main_page import MainPage
from tests.data import CALLBACK_TITLE, HAS_ERROR_NAME


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
        with allure.step('Открываем главную страницу'):
            name_input_send_keys.open()
        with allure.step('Нажимаем на "Заказать обратный звонок"'):
            name_input_send_keys.click_callback_link()
        with allure.step('Заполняем поле "Ваше имя" данными'):
            name_input_send_keys.t_name_input_send_keys(name)
        with allure.step('Заполняем поле "Ваш телефон" данными'):
            name_input_send_keys.phone_input_send_keys()
        with allure.step('Нажимаем кнопку "Отправить заявку"'):
            name_input_send_keys.click_submit_application_button()
        with allure.step('Добавляем ожидание модального окна'):
            name_input_send_keys.wait(popup_back_call)
        with allure.step('Проверяем, что заявка успешно отправлена'):
            assert name_input_send_keys.get_callback_title() == CALLBACK_TITLE

    @allure.title('В форме "Заявка на обратный звонок", удаляем введенные данные из поля "Ваше имя"')
    def test_name_input_delete_send_keys(self, browser):
        name_input_delete = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            name_input_delete.open()
        with allure.step('Нажимаем на "Заказать обратный звонок"'):
            name_input_delete.click_callback_link()
        with allure.step('Вводим в поле "Ваше имя" одну букву'):
            name_input_delete.name_input_send_keys()
        with allure.step('Удаляем введенный текст'):
            name_input_delete.name_input_delete()
        with allure.step('Проверяем, что значение поля изменилось после удаления данных'):
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
        with allure.step('Открываем главную страницу'):
            name_input_send_keys.open()
        with allure.step('Нажимаем на "Заказать обратный звонок"'):
            name_input_send_keys.click_callback_link()
        with allure.step('Заполняем поле "Ваше имя" данными'):
            name_input_send_keys.t_name_input_send_keys(name)
        with allure.step('Ожидаем пока поле "Ваше имя" будет подсвечиваться красным'):
            name_input_send_keys.wait(name_error)
        with allure.step('Проверка наличия класса "has-error"'):
            assert name_input_send_keys.name_input_send_keys_error() == HAS_ERROR_NAME
