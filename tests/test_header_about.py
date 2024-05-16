import allure

from locators.main_page_locators import about, about_list
from pages.anrex_main_page import MainPage
from tests.data import ABOUT, ABOUT_LIST
from tests.urls import URL, CHAPTER_ABOUT, CHAPTER_DEALERS, CHAPTER_CONTACT


class TestHeaderAbout:

    @allure.title('Проверка, что отображается раздел "О компани" в шапке сайта')
    def test_header_about_visibility(self, browser):
        about_visibility = MainPage(browser)
        about_visibility.open()
        assert about_visibility.get_about_text() == ABOUT

    @allure.title('По клику на раздел "О компании", редирект в "Информация о компании"')
    def test_redirection_about(self, browser):
        redirection_delivery = MainPage(browser)
        redirection_delivery.open()
        redirection_delivery.click_about()
        assert redirection_delivery.get_current_url() == f'{URL}{CHAPTER_ABOUT}'

    @allure.title('Проверка, что при наведении на раздел "О компании", появляется выпадающий список')
    def test_about_hover_displays_dropdown(self, browser):
        displays_dropdown = MainPage(browser)
        displays_dropdown.open()
        displays_dropdown.move_cursor_to_element(about)
        assert displays_dropdown.get_elements_text_header(about_list) == ABOUT_LIST

    @allure.title('Проверка, что при снятии фокуса с раздела "О компании", выпадающий список закрывается')
    def test_about_dropdown_closes_on_focus_loss(self, browser):
        closes_on_focus = MainPage(browser)
        closes_on_focus.open()
        closes_on_focus.move_cursor_to_element(about)
        closes_on_focus.defocus_element()
        assert closes_on_focus.get_elements_text_header('') == []

    @allure.title('При нажатии на "Информация о компании" редирект в раздел "Информация о компании"')
    def test_displays_dropdown_redirection_dropdown(self, browser):
        redirection_dropdown = MainPage(browser)
        redirection_dropdown.open()
        redirection_dropdown.move_cursor_to_element(about)
        redirection_dropdown.click_about_dropdown()
        assert redirection_dropdown.get_current_url() == f'{URL}{CHAPTER_ABOUT}'

    @allure.title('При нажатии на "Дилерам" редирект в раздел "Дилерам"')
    def test_displays_dropdown_redirection_dealers(self, browser):
        redirection_dealers = MainPage(browser)
        redirection_dealers.open()
        redirection_dealers.move_cursor_to_element(about)
        redirection_dealers.click_dealers_dropdown()
        assert redirection_dealers.get_current_url() == f'{URL}{CHAPTER_ABOUT}{CHAPTER_DEALERS}'

    @allure.title('При нажатии на "Контакты" редирект в раздел "Контакты"')
    def test_displays_dropdown_redirection_contact(self, browser):
        redirection_contact = MainPage(browser)
        redirection_contact.open()
        redirection_contact.move_cursor_to_element(about)
        redirection_contact.click_contact_dropdown()
        assert redirection_contact.get_current_url() == f'{URL}{CHAPTER_ABOUT}{CHAPTER_CONTACT}'
