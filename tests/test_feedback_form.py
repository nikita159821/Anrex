import allure

from locators.main_page_locators import form_overlay_close
from pages.anrex_main_page import MainPage
from tests.data import TITLE_FORM_FEEDBACK, TEXT_FORM_FEEDBACK, RADIO_BUTTON, NAME_PLACEHOLDER, PHONE_PLACEHOLDER, \
    QUESTION_PLACEHOLDER, EMAIL_PLACEHOLDER


class TestFeedbackForm:

    @allure.title('При нажатии на "Написать нам" появляется форма обратной связи')
    def test_write_us_button_opens_feedback_form(self, browser):
        opens_feedback_form = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            opens_feedback_form.open()
        with allure.step('Скроллим до футера'):
            opens_feedback_form.get_section_footer()
        with allure.step('Нажимаем кнопку "Написать нам"'):
            opens_feedback_form.click_button_write()
        with allure.step('Сохраняем тайтл "Форма обратной связи" - если тайтл есть, форма открыта'):
            assert opens_feedback_form.get_title_form_feedback() == TITLE_FORM_FEEDBACK

    @allure.title('Проверка наличия текста в форме обратной связи')
    def test_feedback_form_description_content(self, browser):
        description_content = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            description_content.open()
        with allure.step('Скроллим до футера'):
            description_content.get_section_footer()
        with allure.step('Нажимаем кнопку "Написать нам"'):
            description_content.click_button_write()
        with allure.step('Сохраняем текст из "Форма обратной связи" и сравниваем с ожидаемым'):
            assert description_content.get_text_form_feedback() == TEXT_FORM_FEEDBACK

    @allure.title('В форме обратной связи отображаются радиокнопки')
    def test_feedback_form_desciption_content(self, browser):
        description_content = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            description_content.open()
        with allure.step('Скроллим до футера'):
            description_content.get_section_footer()
        with allure.step('Нажимаем кнопку "Написать нам"'):
            description_content.click_button_write()
        with allure.step('Сохраняем текст радиокнопок из "Форма обратной связи" и сравниваем с ожидаемым'):
            assert description_content.get_text_radio_buttons() == RADIO_BUTTON

    @allure.title('Форма обратной связи закрывается через крестик')
    def test_feedback_form_close(self, browser):
        form_close = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            form_close.open()
        with allure.step('Скроллим до футера'):
            form_close.get_section_footer()
        with allure.step('Нажимаем кнопку "Написать нам"'):
            form_close.click_button_write()
        with allure.step('Закрываем форму через крестик'):
            form_close.click_form_close()
        with allure.step('Проверяем, если нет тайтла из формы, значит закрыта'):
            assert form_close.get_title_form_feedback() == ''

    @allure.title('Форма обратной связи закрывается через оверлей')
    def test_feedback_form_close_overlay(self, browser):
        form_close_overlay = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            form_close_overlay.open()
        with allure.step('Скроллим до футера'):
            form_close_overlay.get_section_footer()
        with allure.step('Нажимаем кнопку "Написать нам"'):
            form_close_overlay.click_button_write()
        with allure.step('Закрываем форму через оверлей'):
            form_close_overlay.close_modal_via_overlay(form_overlay_close)
        with allure.step('Проверяем, если нет тайтла из формы, значит закрыта'):
            assert form_close_overlay.get_title_form_feedback() == ''

    @allure.title('Форма обратной связи содержит инпут "Ваше Имя"')
    def test_form_feedback_name_input_is_displayed(self, browser):
        form_feedback_name = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            form_feedback_name.open()
        with allure.step('Скроллим до футера'):
            form_feedback_name.get_section_footer()
        with allure.step('Нажимаем кнопку "Написать нам"'):
            form_feedback_name.click_button_write()
        with allure.step('Находим поле "Ваше имя" и проверяем отображение'):
            assert form_feedback_name.get_form_feedback_name_input().is_displayed()

    @allure.title('Форма обратной связи содержит инпут "Ваш телефон"')
    def test_form_feedback_phone_input_is_displayed(self, browser):
        form_feedback_phone = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            form_feedback_phone.open()
        with allure.step('Скроллим до футера'):
            form_feedback_phone.get_section_footer()
        with allure.step('Нажимаем кнопку "Написать нам"'):
            form_feedback_phone.click_button_write()
        with allure.step('Находим поле "Ваш телефон" и проверяем отображение'):
            assert form_feedback_phone.get_form_feedback_phone_input().is_displayed()

    @allure.title('Форма обратной связи содержит инпут "Ваша почта"')
    def test_form_feedback_email_input_is_displayed(self, browser):
        form_feedback_email = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            form_feedback_email.open()
        with allure.step('Скроллим до футера'):
            form_feedback_email.get_section_footer()
        with allure.step('Нажимаем кнопку "Написать нам"'):
            form_feedback_email.click_button_write()
        with allure.step('Находим поле "Ваша почта" и проверяем отображение'):
            assert form_feedback_email.get_form_feedback_email_input().is_displayed()

    @allure.title('Форма обратной связи содержит инпут "Ваш вопрос/комментарий"')
    def test_form_feedback_question_input_is_displayed(self, browser):
        form_feedback_question = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            form_feedback_question.open()
        with allure.step('Скроллим до футера'):
            form_feedback_question.get_section_footer()
        with allure.step('Нажимаем кнопку "Написать нам"'):
            form_feedback_question.click_button_write()
        with allure.step('Находим поле "Ваш вопрос/комментарий" и проверяем отображение'):
            assert form_feedback_question.get_form_feedback_question_input().is_displayed()

    @allure.title('Инпут "Ваше Имя" в Форме обратной связи содержит плейсхолдер')
    def test_placeholder_form_feedback_name_input(self, browser):
        placeholder_form_feedback_name = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            placeholder_form_feedback_name.open()
        with allure.step('Скроллим до футера'):
            placeholder_form_feedback_name.get_section_footer()
        with allure.step('Нажимаем кнопку "Написать нам"'):
            placeholder_form_feedback_name.click_button_write()
        with allure.step('Находим поле "Ваше Имя" и проверяем отображение плейсхолдера'):
            assert placeholder_form_feedback_name.get_placeholder_form_feedback_name_input() == NAME_PLACEHOLDER

    @allure.title('Инпут "Ваш телефон" в Форме обратной связи содержит плейсхолдер')
    def test_placeholder_form_feedback_phone_input(self, browser):
        placeholder_form_feedback_phone = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            placeholder_form_feedback_phone.open()
        with allure.step('Скроллим до футера'):
            placeholder_form_feedback_phone.get_section_footer()
        with allure.step('Нажимаем кнопку "Написать нам"'):
            placeholder_form_feedback_phone.click_button_write()
        with allure.step('Находим поле "Ваш телефон" и проверяем отображение плейсхолдера'):
            assert placeholder_form_feedback_phone.get_placeholder_form_feedback_phone_input() == PHONE_PLACEHOLDER

    @allure.title('Инпут "Ваша почта" в Форме обратной связи содержит плейсхолдер')
    def test_placeholder_form_feedback_email_input(self, browser):
        placeholder_form_feedback_email = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            placeholder_form_feedback_email.open()
        with allure.step('Скроллим до футера'):
            placeholder_form_feedback_email.get_section_footer()
        with allure.step('Нажимаем кнопку "Написать нам"'):
            placeholder_form_feedback_email.click_button_write()
        with allure.step('Находим поле "Ваша почта" и проверяем отображение плейсхолдера'):
            assert placeholder_form_feedback_email.get_placeholder_form_feedback_email_input() == EMAIL_PLACEHOLDER

    @allure.title('Инпут "Ваш вопрос/комментарий*" в Форме обратной связи содержит плейсхолдер')
    def test_placeholder_form_feedback_question_input(self, browser):
        placeholder_form_feedback_question = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            placeholder_form_feedback_question.open()
        with allure.step('Скроллим до футера'):
            placeholder_form_feedback_question.get_section_footer()
        with allure.step('Нажимаем кнопку "Написать нам"'):
            placeholder_form_feedback_question.click_button_write()
        with allure.step('Находим поле "Ваш вопрос/комментарий*" и проверяем отображение плейсхолдера'):
            assert placeholder_form_feedback_question.get_placeholder_form_question_input() == QUESTION_PLACEHOLDER

    @allure.title('Форма обратной связи содержит кнопку "Отправить форму"')
    def test_button_form_feedback_is_displayed(self, browser):
        button_form_feedback = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            button_form_feedback.open()
        with allure.step('Скроллим до футера'):
            button_form_feedback.get_section_footer()
        with allure.step('Нажимаем кнопку "Написать нам"'):
            button_form_feedback.click_button_write()
        with allure.step('Находим кнопку в форме и проверяем отображение'):
            assert button_form_feedback.get_button_form_feedback().is_displayed()
