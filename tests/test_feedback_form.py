import time

from locators.main_page_locators import reviews, test, footer, section_collections
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

    # Форма обратной связи закрывается через крестик
    def test_feedback_form_close(self, browser):
        form_close = MainPage(browser)
        form_close.open()
        form_close.get_section_footer()
        form_close.click_button_write()
        form_close.click_form_close()
        assert form_close.get_title_form_feedback() == ''
        
    # Форма обратной связи закрывается через оверлей
    def test_feedback_form_close_overlay(self,browser):
        form_close_overlay = MainPage(browser)
        form_close_overlay.open()
        form_close_overlay.get_section_footer()
        form_close_overlay.click_button_write()
        time.sleep(3)
        form_close_overlay.close_modal_via_overlay(test)
        time.sleep(5)
