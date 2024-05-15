import pytest

from locators.main_page_locators import popup_form_feedback
from pages.anrex_main_page import MainPage
from tests.data import POPUP_TEXT_FORM_FEEDBACK


class TestNameInputSendKeys:

    # Вводим в поле "Ваше имя" 2 буквы, 49, букв, 50 букв, 51 букву, 10 букв на латинице
    @pytest.mark.parametrize('name', [
        MainPage.generate_name_and_phone(2, 'russian_letters'),
        MainPage.generate_name_and_phone(49, 'russian_letters'),
        MainPage.generate_name_and_phone(50, 'russian_letters'),
        MainPage.generate_name_and_phone(51, 'russian_letters'),
        MainPage.generate_name_and_phone(10, 'letters'),
    ])
    def test_positive_name_input_form_feedback_send_keys(self, browser, name):
        name_input_form_feedback_send_keys = MainPage(browser)
        name_input_form_feedback_send_keys.open()
        name_input_form_feedback_send_keys.get_section_footer()
        name_input_form_feedback_send_keys.click_button_write()
        name_input_form_feedback_send_keys.click_checkbox_radio_button()
        name_input_form_feedback_send_keys.form_name_input_send_keys(name)
        name_input_form_feedback_send_keys.send_keys_input_phone_form_feedback()
        name_input_form_feedback_send_keys.send_keys_input_question_form_feedback()
        name_input_form_feedback_send_keys.click_button_form_feedback()
        name_input_form_feedback_send_keys.wait(popup_form_feedback)
        assert name_input_form_feedback_send_keys.text_popup_form_feedback() == POPUP_TEXT_FORM_FEEDBACK
