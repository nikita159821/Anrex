from locators.main_page_locators import popup_back_call
from pages.anrex_main_page import MainPage
from tests.data import CALLBACK_TITLE


class TestCallbackRequestTests:

    # Отправляем заявку на обратный звонок. Все поля заполнены
    def test_submit_with_all_fields_filled(self, browser):
        submit_with_all = MainPage(browser)
        submit_with_all.open()
        submit_with_all.click_callback_link()
        random_name = submit_with_all.generate_random_string(2, 'russian_letters')
        submit_with_all.t_name_input_send_keys(random_name)
        submit_with_all.phone_input_send_keys()
        submit_with_all.click_submit_application_button()
        submit_with_all.wait(popup_back_call)
        assert submit_with_all.get_callback_title() == CALLBACK_TITLE

    # Отправляем заявку на обратный звонок. Ни одно поле не заполнено
    def test_callback_request_with_empty_fields(self, browser):
        callback_request = MainPage(browser)
        callback_request.open()
        callback_request.click_callback_link()
        callback_request.click_submit_application_button()
        assert not callback_request.get_callback_title_element().is_displayed()

    # Отправляем заявку на обратный звонок. Поле "Ваш телефон" не заполнено
    def test_callback_request_with_empty_phone_field(self, browser):
        phone_field = MainPage(browser)
        phone_field.open()
        phone_field.click_callback_link()
        random_name = phone_field.generate_random_string(2, 'russian_letters')
        phone_field.t_name_input_send_keys(random_name)
        phone_field.click_submit_application_button()
        assert not phone_field.get_callback_title_element().is_displayed()

    # Отправляем заявку на обратный звонок. Поле "Ваше имя" не заполнено
    def test_callback_request_with_empty_name_field(self, browser):
        name_field = MainPage(browser)
        name_field.open()
        name_field.click_callback_link()
        name_field.phone_input_send_keys()
        name_field.click_submit_application_button()
        assert not name_field.get_callback_title_element().is_displayed()
