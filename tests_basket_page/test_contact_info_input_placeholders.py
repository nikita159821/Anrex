import allure
from pages.basket_page import BasketPage
from tests_basket_page.data import INPUT_NAME_PLACEHOLDER, INPUT_ADDRESS_PLACEHOLDER, INPUT_STREET_PLACEHOLDER, \
    INPUT_HOUSE_PLACEHOLDER, INPUT_BUILDING_PLACEHOLDER, INPUT_APARTMENT_PLACEHOLDER, INPUT_PHONE_PLACEHOLDER, \
    INPUT_EMAIL_PLACEHOLDER, INPUT_COMMENT_PLACEHOLDER


class TestBlockContactInputPlaceholders:
    @allure.title('В поле "ФИО" отображается плейсхолдер')
    def test_contact_info_input_name_placeholders(self, browser):
        name_placeholders = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            name_placeholders.open_basket()
        with allure.step('Проверяем отображение плейсхолдера в поле ФИО'):
            assert name_placeholders.get_input_name_placeholder() == INPUT_NAME_PLACEHOLDER

    @allure.title('В поле "Город" отображается плейсхолдер')
    def test_contact_info_input_address_placeholders(self, browser):
        address_placeholders = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            address_placeholders.open_basket()
        with allure.step('Проверяем отображение плейсхолдера в поле Адрес'):
            assert address_placeholders.get_input_address_placeholder() == INPUT_ADDRESS_PLACEHOLDER

    @allure.title('В поле "Улица" отображается плейсхолдер')
    def test_contact_info_input_street_placeholders(self, browser):
        street_placeholders = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            street_placeholders.open_basket()
        with allure.step('Проверяем отображение плейсхолдера в поле Улица'):
            assert street_placeholders.get_input_street_placeholder() == INPUT_STREET_PLACEHOLDER

    @allure.title('В поле "Дом" отображается плейсхолдер')
    def test_contact_info_input_house_placeholders(self, browser):
        house_placeholders = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            house_placeholders.open_basket()
        with allure.step('Проверяем отображение плейсхолдера в поле Дом'):
            assert house_placeholders.get_input_house_placeholder() == INPUT_HOUSE_PLACEHOLDER

    @allure.title('В поле "Корпус" отображается плейсхолдер')
    def test_contact_info_input_building_placeholders(self, browser):
        building_placeholders = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            building_placeholders.open_basket()
        with allure.step('Проверяем отображение плейсхолдера в поле Корпус'):
            assert building_placeholders.get_input_building_placeholder() == INPUT_BUILDING_PLACEHOLDER

    @allure.title('В поле "Квартира" отображается плейсхолдер')
    def test_contact_info_input_apartment_placeholders(self, browser):
        apartment_placeholders = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            apartment_placeholders.open_basket()
        with allure.step('Проверяем отображение плейсхолдера в поле Квартира'):
            assert apartment_placeholders.get_input_apartment_placeholder() == INPUT_APARTMENT_PLACEHOLDER

    @allure.title('В поле "Номер телефона" отображается плейсхолдер')
    def test_contact_info_input_phone_placeholders(self, browser):
        phone_placeholders = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            phone_placeholders.open_basket()
        with allure.step('Проверяем отображение плейсхолдера в поле Номер телефона'):
            assert phone_placeholders.get_input_phone_placeholder() == INPUT_PHONE_PLACEHOLDER

    @allure.title('В поле "E-mail" отображается плейсхолдер')
    def test_contact_info_input_email_placeholders(self, browser):
        email_placeholders = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            email_placeholders.open_basket()
        with allure.step('Проверяем отображение плейсхолдера в поле E-mail'):
            assert email_placeholders.get_input_email_placeholder() == INPUT_EMAIL_PLACEHOLDER

    @allure.title('В поле "E-mail" отображается плейсхолдер')
    def test_contact_info_input_email_placeholders(self, browser):
        comment_placeholders = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            comment_placeholders.open_basket()
        with allure.step('Проверяем отображение плейсхолдера в поле E-mail'):
            assert comment_placeholders.get_input_comment_placeholder() == INPUT_COMMENT_PLACEHOLDER
