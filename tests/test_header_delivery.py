from locators.main_page_locators import delivery, delivery_list
from pages.anrex_main_page import MainPage
from tests.data import DELIVERY, DELIVERY_LIST
from tests.urls import URL, CHAPTER_DELIVERY, CHAPTER_SHOPS, CHAPTER_QUARANTEE


class TestHeaderDelivery:

    # Проверка, что отображается раздел "Покупателям" в шапке сайта
    def test_header_delivery_visibility(self, browser):
        delivery_visibility = MainPage(browser)
        delivery_visibility.open()
        assert delivery_visibility.get_cdelivery_text() == DELIVERY

    # Проверка, что при наведении на раздел "Покупателям", появляется выпадающий список
    def test_delivery_hover_displays_dropdown(self, browser):
        displays_dropdown = MainPage(browser)
        displays_dropdown.open()
        displays_dropdown.move_cursor_to_element(delivery)
        assert displays_dropdown.get_elements_text(delivery_list) == DELIVERY_LIST

    # Проверка, что при снятии фокуса с раздела "Каталог", выпадающий список закрывается
    def test_catalog_dropdown_closes_on_focus_loss(self, browser):
        closes_on_focus = MainPage(browser)
        closes_on_focus.open()
        closes_on_focus.move_cursor_to_element(delivery)
        closes_on_focus.defocus_element()
        assert closes_on_focus.get_elements_text('') == []

    # По клику на раздел "Покупателям", редирект в "Доставка и сборка"
    def test_redirection_delivery(self, browser):
        redirection_delivery = MainPage(browser)
        redirection_delivery.open()
        redirection_delivery.click_delivery()
        assert redirection_delivery.get_current_url() == f'{URL}{CHAPTER_DELIVERY}'

    # При нажатии на "Доставка и сборка" редирект в раздел сборки и доставки
    def test_displays_dropdown_redirection_delivery(self, browser):
        redirection_delivery = MainPage(browser)
        redirection_delivery.open()
        redirection_delivery.move_cursor_to_element(delivery)
        redirection_delivery.click_delivery_dropdown()
        assert redirection_delivery.get_current_url() == f'{URL}{CHAPTER_DELIVERY}'

    # При нажатии на "Гарантия на мебель" редирект в раздел "Гарантия"
    def test_displays_dropdown_redirection_guarantee(self, browser):
        redirection_guarantee = MainPage(browser)
        redirection_guarantee.open()
        redirection_guarantee.move_cursor_to_element(delivery)
        redirection_guarantee.click_guarantee_dropdown()
        assert redirection_guarantee.get_current_url() == f'{URL}{CHAPTER_QUARANTEE}'

    # При нажатии на "Адреса магазинов" редирект в раздел адресов
    def test_displays_dropdown_redirection_shops(self, browser):
        redirection_shops = MainPage(browser)
        redirection_shops.open()
        redirection_shops.move_cursor_to_element(delivery)
        redirection_shops.click_shops_dropdown()
        assert redirection_shops.get_current_url() == f'{URL}{CHAPTER_SHOPS}'
