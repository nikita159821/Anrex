import allure

from locators.main_page_locators import about, about_list
from pages.anrex_main_page import MainPage
from tests_main_page.data import ABOUT, ABOUT_LIST
from tests_main_page.urls import URL, CHAPTER_ABOUT, CHAPTER_DEALERS, CHAPTER_CONTACT


class TestHeaderAbout:

    @allure.title('Проверка, что отображается раздел "О компани" в шапке сайта')
    def test_header_about_visibility(self, browser):
        about_visibility = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            about_visibility.open()
        with allure.step('Получаем текст "О компании" и сравниваем с ожидаемым'):
            assert about_visibility.get_about_text() == ABOUT

    @allure.title('По клику на раздел "О компании", редирект в "Информация о компании"')
    def test_redirection_about(self, browser):
        redirection_delivery = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            redirection_delivery.open()
        with allure.step('Нажимаем на раздел "О компании"'):
            redirection_delivery.click_about()
        with allure.step('Проверяем переход на страницу "О компании"'):
            assert redirection_delivery.get_current_url() == f'{URL}{CHAPTER_ABOUT}'

    @allure.title('Проверка, что при наведении на раздел "О компании", появляется выпадающий список')
    def test_about_hover_displays_dropdown(self, browser):
        displays_dropdown = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            displays_dropdown.open()
        with allure.step('Наводим курсор на раздел "О компании"'):
            displays_dropdown.move_cursor_to_element(about)
        with allure.step('Проверяем, что отображаются другие разделы и сравниваем с ожидаемыми'):
            assert displays_dropdown.get_elements_text_header(about_list) == ABOUT_LIST

    @allure.title('Проверка, что при снятии фокуса с раздела "О компании", выпадающий список закрывается')
    def test_about_dropdown_closes_on_focus_loss(self, browser):
        closes_on_focus = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            closes_on_focus.open()
        with allure.step('Наводим курсор на раздел "О компании"'):
            closes_on_focus.move_cursor_to_element(about)
        with allure.step('Снимает фокус с раздела "О компании"'):
            closes_on_focus.defocus_element()
        with allure.step('Проверяем, что выпадающий список закрыл. Если не получили другие разделы - пройдено'):
            assert closes_on_focus.get_elements_text_header('') == []

    @allure.title('При нажатии на "Информация о компании" редирект в раздел "Информация о компании"')
    def test_displays_dropdown_redirection_dropdown(self, browser):
        redirection_dropdown = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            redirection_dropdown.open()
        with allure.step('Наводим курсор на раздел "О компании"'):
            redirection_dropdown.move_cursor_to_element(about)
        with allure.step('Нажимаем на раздел "Информация о компании" в выпадающем списке"'):
            redirection_dropdown.click_about_dropdown()
        with allure.step('Проверям открытие раздела "Информация о компании"'):
            assert redirection_dropdown.get_current_url() == f'{URL}{CHAPTER_ABOUT}'

    @allure.title('При нажатии на "Дилерам" редирект в раздел "Дилерам"')
    def test_displays_dropdown_redirection_dealers(self, browser):
        redirection_dealers = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            redirection_dealers.open()
        with allure.step('Наводим курсор на раздел "О компании"'):
            redirection_dealers.move_cursor_to_element(about)
        with allure.step('Нажимаем на раздел "Дилерам" в выпадающем списке"'):
            redirection_dealers.click_dealers_dropdown()
        with allure.step('Проверям открытие раздела "Дилерам"'):
            assert redirection_dealers.get_current_url() == f'{URL}{CHAPTER_ABOUT}{CHAPTER_DEALERS}'

    @allure.title('При нажатии на "Контакты" редирект в раздел "Контакты"')
    def test_displays_dropdown_redirection_contact(self, browser):
        redirection_contact = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            redirection_contact.open()
        with allure.step('Наводим курсор на раздел "О компании"'):
            redirection_contact.move_cursor_to_element(about)
        with allure.step('Нажимаем на раздел "Контакты" в выпадающем списке"'):
            redirection_contact.click_contact_dropdown()
        with allure.step('Проверям открытие раздела "Контакты"'):
            assert redirection_contact.get_current_url() == f'{URL}{CHAPTER_ABOUT}{CHAPTER_CONTACT}'
