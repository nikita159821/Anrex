import allure

from locators.main_page_locators import basket_count, button_card
from pages.basket_page import BasketPage
from tests_basket_page.data import INPUT_NAME_PLACEHOLDER, INPUT_ADDRESS_PLACEHOLDER, INPUT_STREET_PLACEHOLDER, \
    INPUT_HOUSE_PLACEHOLDER, INPUT_BUILDING_PLACEHOLDER, INPUT_APARTMENT_PLACEHOLDER, INPUT_PHONE_PLACEHOLDER, \
    INPUT_EMAIL_PLACEHOLDER, INPUT_COMMENT_PLACEHOLDER


class TestBlockContactInputPlaceholders:
    @allure.title('В поле "ФИО" отображается плейсхолдер')
    def test_contact_info_input_name_placeholders(self, browser):
        name_placeholders = BasketPage(browser)
        with allure.step('Открываем страницу каталога'):
            name_placeholders.open_catalog()
        with allure.step('Скроллим до карточки товара'):
            name_placeholders.get_element_scroll_to_element(button_card)
        with allure.step('Нажимаем "Добавить в корзину" у карточки товара'):
            name_placeholders.button_click_cards()
        with allure.step('Ждем пока товар добавится в корзину'):
            name_placeholders.wait_for_element(basket_count)
        with allure.step('Нажимаем на иконку корзины'):
            name_placeholders.sale_basket_click()
        with allure.step('Проверяем отображение плейсхолдера в поле ФИО'):
            assert name_placeholders.get_input_name_placeholder() == INPUT_NAME_PLACEHOLDER

    @allure.title('В поле "Адрес" отображается плейсхолдер')
    def test_contact_info_input_address_placeholders(self, browser):
        address_placeholders = BasketPage(browser)
        with allure.step('Открываем страницу каталога'):
            address_placeholders.open_catalog()
        with allure.step('Скроллим до карточки товара'):
            address_placeholders.get_element_scroll_to_element(button_card)
        with allure.step('Нажимаем "Добавить в корзину" у карточки товара'):
            address_placeholders.button_click_cards()
        with allure.step('Ждем пока товар добавится в корзину'):
            address_placeholders.wait_for_element(basket_count)
        with allure.step('Нажимаем на иконку корзины'):
            address_placeholders.sale_basket_click()
        with allure.step('Проверяем отображение плейсхолдера в поле Адрес'):
            assert address_placeholders.get_input_address_placeholder() == INPUT_ADDRESS_PLACEHOLDER

    @allure.title('В поле "Улица" отображается плейсхолдер')
    def test_contact_info_input_street_placeholders(self, browser):
        street_placeholders = BasketPage(browser)
        with allure.step('Открываем страницу каталога'):
            street_placeholders.open_catalog()
        with allure.step('Скроллим до карточки товара'):
            street_placeholders.get_element_scroll_to_element(button_card)
        with allure.step('Нажимаем "Добавить в корзину" у карточки товара'):
            street_placeholders.button_click_cards()
        with allure.step('Ждем пока товар добавится в корзину'):
            street_placeholders.wait_for_element(basket_count)
        with allure.step('Нажимаем на иконку корзины'):
            street_placeholders.sale_basket_click()
        with allure.step('Проверяем отображение плейсхолдера в поле Улица'):
            assert street_placeholders.get_input_street_placeholder() == INPUT_STREET_PLACEHOLDER

    @allure.title('В поле "Дом" отображается плейсхолдер')
    def test_contact_info_input_house_placeholders(self, browser):
        house_placeholders = BasketPage(browser)
        with allure.step('Открываем страницу каталога'):
            house_placeholders.open_catalog()
        with allure.step('Скроллим до карточки товара'):
            house_placeholders.get_element_scroll_to_element(button_card)
        with allure.step('Нажимаем "Добавить в корзину" у карточки товара'):
            house_placeholders.button_click_cards()
        with allure.step('Ждем пока товар добавится в корзину'):
            house_placeholders.wait_for_element(basket_count)
        with allure.step('Нажимаем на иконку корзины'):
            house_placeholders.sale_basket_click()
        with allure.step('Проверяем отображение плейсхолдера в поле Дом'):
            assert house_placeholders.get_input_house_placeholder() == INPUT_HOUSE_PLACEHOLDER

    @allure.title('В поле "Корпус" отображается плейсхолдер')
    def test_contact_info_input_building_placeholders(self, browser):
        building_placeholders = BasketPage(browser)
        with allure.step('Открываем страницу каталога'):
            building_placeholders.open_catalog()
        with allure.step('Скроллим до карточки товара'):
            building_placeholders.get_element_scroll_to_element(button_card)
        with allure.step('Нажимаем "Добавить в корзину" у карточки товара'):
            building_placeholders.button_click_cards()
        with allure.step('Ждем пока товар добавится в корзину'):
            building_placeholders.wait_for_element(basket_count)
        with allure.step('Нажимаем на иконку корзины'):
            building_placeholders.sale_basket_click()
        with allure.step('Проверяем отображение плейсхолдера в поле Корпус'):
            assert building_placeholders.get_input_building_placeholder() == INPUT_BUILDING_PLACEHOLDER

    @allure.title('В поле "Квартира" отображается плейсхолдер')
    def test_contact_info_input_apartment_placeholders(self, browser):
        apartment_placeholders = BasketPage(browser)
        with allure.step('Открываем страницу каталога'):
            apartment_placeholders.open_catalog()
        with allure.step('Скроллим до карточки товара'):
            apartment_placeholders.get_element_scroll_to_element(button_card)
        with allure.step('Нажимаем "Добавить в корзину" у карточки товара'):
            apartment_placeholders.button_click_cards()
        with allure.step('Ждем пока товар добавится в корзину'):
            apartment_placeholders.wait_for_element(basket_count)
        with allure.step('Нажимаем на иконку корзины'):
            apartment_placeholders.sale_basket_click()
        with allure.step('Проверяем отображение плейсхолдера в поле Квартира'):
            assert apartment_placeholders.get_input_apartment_placeholder() == INPUT_APARTMENT_PLACEHOLDER

    @allure.title('В поле "Номер телефона" отображается плейсхолдер')
    def test_contact_info_input_phone_placeholders(self, browser):
        phone_placeholders = BasketPage(browser)
        with allure.step('Открываем страницу каталога'):
            phone_placeholders.open_catalog()
        with allure.step('Скроллим до карточки товара'):
            phone_placeholders.get_element_scroll_to_element(button_card)
        with allure.step('Нажимаем "Добавить в корзину" у карточки товара'):
            phone_placeholders.button_click_cards()
        with allure.step('Ждем пока товар добавится в корзину'):
            phone_placeholders.wait_for_element(basket_count)
        with allure.step('Нажимаем на иконку корзины'):
            phone_placeholders.sale_basket_click()
        with allure.step('Проверяем отображение плейсхолдера в поле Номер телефона'):
            assert phone_placeholders.get_input_phone_placeholder() == INPUT_PHONE_PLACEHOLDER

    @allure.title('В поле "E-mail" отображается плейсхолдер')
    def test_contact_info_input_email_placeholders(self, browser):
        email_placeholders = BasketPage(browser)
        with allure.step('Открываем страницу каталога'):
            email_placeholders.open_catalog()
        with allure.step('Скроллим до карточки товара'):
            email_placeholders.get_element_scroll_to_element(button_card)
        with allure.step('Нажимаем "Добавить в корзину" у карточки товара'):
            email_placeholders.button_click_cards()
        with allure.step('Ждем пока товар добавится в корзину'):
            email_placeholders.wait_for_element(basket_count)
        with allure.step('Нажимаем на иконку корзины'):
            email_placeholders.sale_basket_click()
        with allure.step('Проверяем отображение плейсхолдера в поле E-mail'):
            assert email_placeholders.get_input_email_placeholder() == INPUT_EMAIL_PLACEHOLDER

    @allure.title('В поле "E-mail" отображается плейсхолдер')
    def test_contact_info_input_email_placeholders(self, browser):
        comment_placeholders = BasketPage(browser)
        with allure.step('Открываем страницу каталога'):
            comment_placeholders.open_catalog()
        with allure.step('Скроллим до карточки товара'):
            comment_placeholders.get_element_scroll_to_element(button_card)
        with allure.step('Нажимаем "Добавить в корзину" у карточки товара'):
            comment_placeholders.button_click_cards()
        with allure.step('Ждем пока товар добавится в корзину'):
            comment_placeholders.wait_for_element(basket_count)
        with allure.step('Нажимаем на иконку корзины'):
            comment_placeholders.sale_basket_click()
        with allure.step('Проверяем отображение плейсхолдера в поле E-mail'):
            assert comment_placeholders.get_input_comment_placeholder() == INPUT_COMMENT_PLACEHOLDER
