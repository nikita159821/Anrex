import time

from pages.anrex_main_page import MainPage
from tests.data import TITLE_FORM_FEEDBACK, TEXT_FORM_FEEDBACK, RADIO_BUTTON


class TestFeedbackForm:

    # При нажатии на "Написать нам" появляется форма обратной связи
    def test_write_us_button_opens_feedback_form(self, browser):
        opens_feedback_form = MainPage(browser)
        opens_feedback_form.open()
        opens_feedback_form.get_section_footer()
        opens_feedback_form.click_button_write()
        assert opens_feedback_form.get_title_form_feedback() == TITLE_FORM_FEEDBACK

    # Проверка наличия текста в форме обратной связи
    def test_feedback_form_description_content(self, browser):
        description_content = MainPage(browser)
        description_content.open()
        description_content.get_section_footer()
        description_content.click_button_write()
        assert description_content.get_text_form_feedback() == TEXT_FORM_FEEDBACK

    # В форме обратной связи отображаются радиокнопки
    def test_feedback_form_desciption_content(self, browser):
        description_content = MainPage(browser)
        description_content.open()
        description_content.get_section_footer()
        description_content.click_button_write()
        assert description_content.get_text_radio_buttons() == RADIO_BUTTON
