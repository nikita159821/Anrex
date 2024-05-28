import allure
import pytest

from locators.main_page_locators import email_error
from pages.anrex_main_page import MainPage
from tests.data import HAS_ERROR_EMAIL


class TestEmailInputSendKeys:

    # Вводим в поле "Ваша почта" Email в верхнем регистре, с цифрами в имени аккаунта,
    # с дефисом в имени аккаунта, со знаком подчеркивания в имени аккаунта, с точками в имени аккаунта
    @pytest.mark.parametrize('email', [
        MainPage.generate_random_string(5, 'letters').upper() + '@example.com',
        MainPage.generate_random_string(3, 'digits') + MainPage.generate_random_string(3, 'letters') + '@example.com',
        MainPage.generate_random_string(3, 'letters') + '-' + MainPage.generate_random_string(3,
                                                                                              'letters') + '@example.com',
        MainPage.generate_random_string(3, 'letters') + '_' + MainPage.generate_random_string(3,
                                                                                              'letters') + '@example.com',
        MainPage.generate_random_string(3, 'letters') + '.' + MainPage.generate_random_string(3,
                                                                                              'letters') + '@example.com',
    ])
    @allure.title('Ввод почты в форме обратной связи')
    def test_positive_email_input_form_feedback_send_keys(self, browser, email):
        email_input_form_feedback_send_keys = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            email_input_form_feedback_send_keys.open()
        with allure.step('Скроллим до футера'):
            email_input_form_feedback_send_keys.get_section_footer()
        with allure.step('Нажимаем кнопку "Написать нам"'):
            email_input_form_feedback_send_keys.click_button_write()
        with allure.step('Вводим почту в поле "Ваша почта"'):
            email_input_form_feedback_send_keys.form_email_input_send_keys(email)
        with allure.step('Находим поле "Ваша почта"'):
            email_input = email_input_form_feedback_send_keys.get_form_feedback_email_input()
        with allure.step('Получаем текущее значение поля "Ваша почта"'):
            current_value = email_input.get_attribute("value")
        with allure.step('Сравниваем значение поля "Ваша почта" с ожидаемым'):
            assert email_input.get_attribute("value") == current_value

    # Вводим в поле "Ваша почта" без @ в email, Email без доменной части
    @pytest.mark.parametrize('email', [
        MainPage.generate_random_string(5, 'letters').upper() + 'example.com',  # Без @ в email
        MainPage.generate_random_string(10, 'letters')  # Без доменной части
    ])
    @allure.title('Ввод почты в форме обратной связи')
    def test_negative_email_input_form_feedback_send_keys(self, browser, email):
        email_input_form_feedback_send_keys = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            email_input_form_feedback_send_keys.open()
        with allure.step('Скроллим до футера'):
            email_input_form_feedback_send_keys.get_section_footer()
        with allure.step('Нажимаем кнопку "Написать нам"'):
            email_input_form_feedback_send_keys.click_button_write()
        with allure.step('Вводим почту в поле "Ваша почта"'):
            email_input_form_feedback_send_keys.form_email_input_send_keys(email)
        with allure.step('Ожидаем пока поле "Ваше имя" будет подсвечиваться красным'):
            email_input_form_feedback_send_keys.wait(email_error)
        with allure.step('Проверка наличия класса "has-error"'):
            assert email_input_form_feedback_send_keys.email_input_send_keys_error() == HAS_ERROR_EMAIL

    @allure.title('Ввод почты с пробелами в имени аккаунта.Форма обратной связи')
    def test_form_feedback_invalid_email_input(self, browser):
        invalid_email = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            invalid_email.open()
        with allure.step('Скроллим до футера'):
            invalid_email.get_section_footer()
        with allure.step('Нажимаем кнопку "Написать нам"'):
            invalid_email.click_button_write()
        with allure.step('Вводим почту c пробелом в поле "Ваша почта"'):
            invalid_email.form_email_input_send_keys('lxg Xrn@example.com')
        with allure.step('Находим поле "Ваша почта"'):
            email_input = invalid_email.get_form_feedback_email_input()
        with allure.step('Получаем текущее значение поля "Ваша почта"'):
            current_value = email_input.get_attribute("value")
        with allure.step('Сравниваем значение поля "Ваша почта". Пробел удалился.'):
            assert email_input.get_attribute("value") == current_value
