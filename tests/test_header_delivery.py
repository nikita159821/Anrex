import allure

from locators.main_page_locators import delivery, delivery_list
from pages.anrex_main_page import MainPage
from tests.data import DELIVERY, DELIVERY_LIST
from tests.urls import URL, CHAPTER_DELIVERY, CHAPTER_SHOPS, CHAPTER_QUARANTEE


class TestHeaderDelivery:

    @allure.title('Проверка, что отображается раздел "Покупателям" в шапке сайта')
    def test_header_delivery_visibility(self, browser):
        delivery_visibility = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            delivery_visibility.open()
        with allure.step('Получаем текст раздела "Покупателям"'):
            assert delivery_visibility.get_cdelivery_text() == DELIVERY

    @allure.title('При наведении на раздел "Покупателям", появляется выпадающий список')
    def test_delivery_hover_displays_dropdown(self, browser):
        displays_dropdown = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            displays_dropdown.open()
        with allure.step('Наводим курсор на раздел "Покупателям"'):
            displays_dropdown.move_cursor_to_element(delivery)
        with allure.step('Получаем список разделов и сравниваем с ожидаемым'):
            assert displays_dropdown.get_elements_text_header(delivery_list) == DELIVERY_LIST

    @allure.title('При снятии фокуса с раздела "Покупателям", выпадающий список закрывается')
    def test_catalog_dropdown_closes_on_focus_loss(self, browser):
        closes_on_focus = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            closes_on_focus.open()
        with allure.step('Наводим курсор на раздел "Покупателям"'):
            closes_on_focus.move_cursor_to_element(delivery)
        with allure.step('Снимаем курсор с раздела "Покупателям"'):
            closes_on_focus.defocus_element()
        with allure.step(
                'Проверяем, что выпадающий список закрылся. Получаем список разделов и сравниваем с ожидаемым'):
            assert closes_on_focus.get_elements_text_header('') == []

    @allure.title('По клику на раздел "Покупателям", редирект в "Доставка и сборка"')
    def test_redirection_delivery(self, browser):
        redirection_delivery = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            redirection_delivery.open()
        with allure.step('Нажимаем на раздел "Покупателям"'):
            redirection_delivery.click_delivery()
        with allure.step('Проверяем, что открылся раздел "Покупателям"'):
            assert redirection_delivery.get_current_url() == f'{URL}{CHAPTER_DELIVERY}'

    @allure.title('При нажатии на "Доставка и сборка" редирект в раздел сборки и доставки')
    def test_displays_dropdown_redirection_delivery(self, browser):
        redirection_delivery = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            redirection_delivery.open()
        with allure.step('Наводим курсор на раздел "Покупателям"'):
            redirection_delivery.move_cursor_to_element(delivery)
        with allure.step('Нажимаем на раздел "Доставка и сборка"'):
            redirection_delivery.click_delivery_dropdown()
        with allure.step('Проверяем, что открылся раздел "Доставка и сборка"'):
            assert redirection_delivery.get_current_url() == f'{URL}{CHAPTER_DELIVERY}'

    @allure.title('При нажатии на "Гарантия на мебель" редирект в раздел "Гарантия"')
    def test_displays_dropdown_redirection_guarantee(self, browser):
        redirection_guarantee = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            redirection_guarantee.open()
        with allure.step('Наводим курсор на раздел "Покупателям"'):
            redirection_guarantee.move_cursor_to_element(delivery)
        with allure.step('Нажимаем на раздел "Гарантия на мебель"'):
            redirection_guarantee.click_guarantee_dropdown()
        with allure.step('Проверяем, что открылся раздел "Гарантия на мебель"'):
            assert redirection_guarantee.get_current_url() == f'{URL}{CHAPTER_QUARANTEE}'

    @allure.title('При нажатии на "Адреса магазинов" редирект в раздел адресов')
    def test_displays_dropdown_redirection_shops(self, browser):
        redirection_shops = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            redirection_shops.open()
        with allure.step('Наводим курсор на раздел "Адреса магазинов"'):
            redirection_shops.move_cursor_to_element(delivery)
        with allure.step('Нажимаем на раздел "Адреса магазинов"'):
            redirection_shops.click_shops_dropdown()
        with allure.step('Проверяем, что открылся раздел "Адреса магазинов"'):
            assert redirection_shops.get_current_url() == f'{URL}{CHAPTER_SHOPS}'
