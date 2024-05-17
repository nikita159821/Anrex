import allure

from locators.main_page_locators import popup_back_call
from pages.anrex_main_page import MainPage
from tests.data import CALLBACK_TITLE


class TestCallbackRequestTests:

    @allure.title('Оформление заявки на обратный звонок. Все поля заполнены')
    def test_submit_with_all_fields_filled(self, browser):
        submit_with_all = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            submit_with_all.open()
        with allure.step('Нажимаем "Заказать обратный звонок"'):
            submit_with_all.click_callback_link()
        with allure.step('Генерируем два буквы'):
            random_name = submit_with_all.generate_random_string(2, 'russian_letters')
        with allure.step('Вводим сгенерированные две буквы в поле "Ваше имя'):
            submit_with_all.t_name_input_send_keys(random_name)
        with allure.step('Вводим номер телефона в поле "Ваш телефон'):
            submit_with_all.phone_input_send_keys()
        with allure.step('Нажимаем кнопку "Отправить заявку"'):
            submit_with_all.click_submit_application_button()
        with allure.step('Ожидание модального окна'):
            submit_with_all.wait(popup_back_call)
        with allure.step('Сравниваем текст в модальном окне с ожидаемым'):
            assert submit_with_all.get_callback_title() == CALLBACK_TITLE

    @allure.title('Оформление заявки на обратный звонок. Ни одно поле не заполнено')
    def test_callback_request_with_empty_fields(self, browser):
        callback_request = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            callback_request.open()
        with allure.step('Нажимаем "Заказать обратный звонок"'):
            callback_request.click_callback_link()
        with allure.step('Нажимаем кнопку "Отправить заявку"'):
            callback_request.click_submit_application_button()
        with allure.step('Проверяем, что заявка не отправлена. Модальное окно не отображается'):
            assert not callback_request.get_callback_title_element().is_displayed()

    @allure.title('Оформление заявки на обратный звонок. Поле "Ваш телефон" не заполнено')
    def test_callback_request_with_empty_phone_field(self, browser):
        phone_field = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            phone_field.open()
        with allure.step('Нажимаем "Заказать обратный звонок"'):
            phone_field.click_callback_link()
        with allure.step('Генерируем два буквы'):
            random_name = phone_field.generate_random_string(2, 'russian_letters')
        with allure.step('Вводим сгенерированные две буквы в поле "Ваше имя'):
            phone_field.t_name_input_send_keys(random_name)
        with allure.step('Нажимаем кнопку "Отправить заявку"'):
            phone_field.click_submit_application_button()
        with allure.step('Проверяем, что заявка не отправлена. Модальное окно не отображается'):
            assert not phone_field.get_callback_title_element().is_displayed()

    @allure.title('Оформление заявки на обратный звонок. Поле "Ваше имя" не заполнено')
    def test_callback_request_with_empty_name_field(self, browser):
        name_field = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            name_field.open()
        with allure.step('Нажимаем "Заказать обратный звонок"'):
            name_field.click_callback_link()
        with allure.step('Вводим номер телефона в поле "Ваш телефон'):
            name_field.phone_input_send_keys()
        with allure.step('Нажимаем кнопку "Отправить заявку"'):
            name_field.click_submit_application_button()
        with allure.step('Проверяем, что заявка не отправлена. Модальное окно не отображается'):
            assert not name_field.get_callback_title_element().is_displayed()
