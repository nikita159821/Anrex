import allure

from locators.main_page_locators import button_write
from pages.anrex_main_page import MainPage
from tests.data import TITLE_BUTTON_FOOTER


class TestFooterButton:

    @allure.title('футере отображается кнопка "Написать нам"')
    def test_footer_write_us_button(self, browser):
        write_us_button = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            write_us_button.open()
        with allure.step('Скроллим до футера'):
            write_us_button.get_section_footer()
        with allure.step('Добавляем ожидание после скролла'):
            write_us_button.wait_for_element(button_write)
        with allure.step('Находим кнопку "Написать нам" и получем её текст. Сравниваем с ожидаемым'):
            assert write_us_button.get_text_button_write() == TITLE_BUTTON_FOOTER
