from locators.main_page_locators import form_overlay_close
from pages.anrex_main_page import MainPage
from tests.data import TITLE_FORM_FEEDBACK, TEXT_FORM_FEEDBACK, RADIO_BUTTON, NAME_PLACEHOLDER, PHONE_PLACEHOLDER, \
    QUESTION_PLACEHOLDER, EMAIL_PLACEHOLDER


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
    def test_feedback_form_close_overlay(self, browser):
        form_close_overlay = MainPage(browser)
        form_close_overlay.open()
        form_close_overlay.get_section_footer()
        form_close_overlay.click_button_write()
        form_close_overlay.close_modal_via_overlay(form_overlay_close)
        assert form_close_overlay.get_title_form_feedback() == ''

    # Форма обратной связи содержит инпут "Ваше Имя"
    def test_form_feedback_name_input_is_displayed(self, browser):
        form_feedback_name = MainPage(browser)
        form_feedback_name.open()
        form_feedback_name.get_section_footer()
        form_feedback_name.click_button_write()
        assert form_feedback_name.get_form_feedback_name_input().is_displayed()

    # Форма обратной связи содержит инпут "Ваш телефон"
    def test_form_feedback_phone_input_is_displayed(self, browser):
        form_feedback_phone = MainPage(browser)
        form_feedback_phone.open()
        form_feedback_phone.get_section_footer()
        form_feedback_phone.click_button_write()
        assert form_feedback_phone.get_form_feedback_phone_input().is_displayed()

    # Форма обратной связи содержит инпут "Ваша почта"
    def test_form_feedback_email_input_is_displayed(self, browser):
        form_feedback_email = MainPage(browser)
        form_feedback_email.open()
        form_feedback_email.get_section_footer()
        form_feedback_email.click_button_write()
        assert form_feedback_email.get_form_feedback_email_input().is_displayed()

    # Форма обратной связи содержит инпут "Ваш вопрос/комментарий"
    def test_form_feedback_question_input_is_displayed(self, browser):
        form_feedback_question = MainPage(browser)
        form_feedback_question.open()
        form_feedback_question.get_section_footer()
        form_feedback_question.click_button_write()
        assert form_feedback_question.get_form_feedback_question_input().is_displayed()

    # Инпут "Ваше Имя" в Форме обратной связи содержит плейсхолдер
    def test_placeholder_form_feedback_name_input(self, browser):
        placeholder_form_feedback_name = MainPage(browser)
        placeholder_form_feedback_name.open()
        placeholder_form_feedback_name.get_section_footer()
        placeholder_form_feedback_name.click_button_write()
        assert placeholder_form_feedback_name.get_placeholder_form_feedback_name_input() == NAME_PLACEHOLDER

    # Инпут "Ваше телефон" в Форме обратной связи содержит плейсхолдер
    def test_placeholder_form_feedback_phone_input(self, browser):
        placeholder_form_feedback_phone = MainPage(browser)
        placeholder_form_feedback_phone.open()
        placeholder_form_feedback_phone.get_section_footer()
        placeholder_form_feedback_phone.click_button_write()
        assert placeholder_form_feedback_phone.get_placeholder_form_feedback_phone_input() == PHONE_PLACEHOLDER

    # Инпут "Ваша почта" в Форме обратной связи содержит плейсхолдер
    def test_placeholder_form_feedback_email_input(self, browser):
        placeholder_form_feedback_email = MainPage(browser)
        placeholder_form_feedback_email.open()
        placeholder_form_feedback_email.get_section_footer()
        placeholder_form_feedback_email.click_button_write()
        assert placeholder_form_feedback_email.get_placeholder_form_feedback_email_input() == EMAIL_PLACEHOLDER

    # Инпут "Ваш вопрос/комментарий*" в Форме обратной связи содержит плейсхолдер
    def test_placeholder_form_feedback_question_input(self, browser):
        placeholder_form_feedback_phone = MainPage(browser)
        placeholder_form_feedback_phone.open()
        placeholder_form_feedback_phone.get_section_footer()
        placeholder_form_feedback_phone.click_button_write()
        assert placeholder_form_feedback_phone.get_placeholder_form_question_input() == QUESTION_PLACEHOLDER

    # Форма обратной связи содержит кнопку "Отправить форму"
    def test_button_form_feedback_is_displayed(self, browser):
        button_form_feedback = MainPage(browser)
        button_form_feedback.open()
        button_form_feedback.get_section_footer()
        button_form_feedback.click_button_write()
        assert button_form_feedback.get_button_form_feedback().is_displayed()
