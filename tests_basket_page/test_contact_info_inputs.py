import allure

from locators.main_page_locators import basket_count
from pages.basket_page import BasketPage
from tests_basket_page.data import INPUT_FULL_NAME, INPUT_DELIVERY_CITY, INPUT_STREET, INPUT_HOUSE, INPUT_BODY, \
    INPUT_FLAT, INPUT_PHONE_NUMBER, INPUT_MAIL, INPUT_YOUR_COMMENT


class TestBlockContactInput:
    @allure.title('В блоке "Контактные данные" отображается инпут "ФИО"')
    def test_contact_info_block_contains_full_name_input(self, browser):
        block_contains_full_name = BasketPage(browser)
        with allure.step('Открываем страницу каталога'):
            block_contains_full_name.open_catalog()
        with allure.step('Нажимаем "Добавить в корзину" у карточки товара'):
            block_contains_full_name.button_click_cards()
        with allure.step('Ждем пока товар добавится в корзину'):
            block_contains_full_name.wait_for_element(basket_count)
        with allure.step('Нажимаем на иконку корзины'):
            block_contains_full_name.sale_basket_click()
        with allure.step('Проверяем отображение поля ФИО'):
            assert block_contains_full_name.get_input_full_name() == INPUT_FULL_NAME

    @allure.title('В блоке "Контактные данные" отображается инпут "Город доставки"')
    def test_contact_info_block_contains_delivery_city_input(self, browser):
        block_contains_delivery_city = BasketPage(browser)
        with allure.step('Открываем страницу каталога'):
            block_contains_delivery_city.open_catalog()
        with allure.step('Нажимаем "Добавить в корзину" у карточки товара'):
            block_contains_delivery_city.button_click_cards()
        with allure.step('Ждем пока товар добавится в корзину'):
            block_contains_delivery_city.wait_for_element(basket_count)
        with allure.step('Нажимаем на иконку корзины'):
            block_contains_delivery_city.sale_basket_click()
        with allure.step('Проверяем отображение поля Город доставки'):
            assert block_contains_delivery_city.get_input_delivery_city() == INPUT_DELIVERY_CITY

    @allure.title('В блоке "Контактные данные" отображается инпут "Улица"')
    def test_contact_info_block_contains_street_input(self, browser):
        block_contains_street = BasketPage(browser)
        with allure.step('Открываем страницу каталога'):
            block_contains_street.open_catalog()
        with allure.step('Нажимаем "Добавить в корзину" у карточки товара'):
            block_contains_street.button_click_cards()
        with allure.step('Ждем пока товар добавится в корзину'):
            block_contains_street.wait_for_element(basket_count)
        with allure.step('Нажимаем на иконку корзины'):
            block_contains_street.sale_basket_click()
        with allure.step('Проверяем отображение поля Улица'):
            assert block_contains_street.get_input_street() == INPUT_STREET

    @allure.title('В блоке "Контактные данные" отображается инпут "Дом"')
    def test_contact_info_block_contains_house_input(self, browser):
        block_contains_house = BasketPage(browser)
        with allure.step('Открываем страницу каталога'):
            block_contains_house.open_catalog()
        with allure.step('Нажимаем "Добавить в корзину" у карточки товара'):
            block_contains_house.button_click_cards()
        with allure.step('Ждем пока товар добавится в корзину'):
            block_contains_house.wait_for_element(basket_count)
        with allure.step('Нажимаем на иконку корзины'):
            block_contains_house.sale_basket_click()
        with allure.step('Проверяем отображение поля Дом'):
            assert block_contains_house.get_input_house() == INPUT_HOUSE

    @allure.title('В блоке "Контактные данные" отображается инпут "Корпус"')
    def test_contact_info_block_contains_body_input(self, browser):
        block_contains_body = BasketPage(browser)
        with allure.step('Открываем страницу каталога'):
            block_contains_body.open_catalog()
        with allure.step('Нажимаем "Добавить в корзину" у карточки товара'):
            block_contains_body.button_click_cards()
        with allure.step('Ждем пока товар добавится в корзину'):
            block_contains_body.wait_for_element(basket_count)
        with allure.step('Нажимаем на иконку корзины'):
            block_contains_body.sale_basket_click()
        with allure.step('Проверяем отображение поля Корпус'):
            assert block_contains_body.get_input_body() == INPUT_BODY

    @allure.title('В блоке "Контактные данные" отображается инпут "Квартира"')
    def test_contact_info_block_contains_flat_input(self, browser):
        block_contains_flat = BasketPage(browser)
        with allure.step('Открываем страницу каталога'):
            block_contains_flat.open_catalog()
        with allure.step('Нажимаем "Добавить в корзину" у карточки товара'):
            block_contains_flat.button_click_cards()
        with allure.step('Ждем пока товар добавится в корзину'):
            block_contains_flat.wait_for_element(basket_count)
        with allure.step('Нажимаем на иконку корзины'):
            block_contains_flat.sale_basket_click()
        with allure.step('Проверяем отображение поля Квартира'):
            assert block_contains_flat.get_input_flat() == INPUT_FLAT

    @allure.title('В блоке "Контактные данные" отображается инпут "Номер телефона"')
    def test_contact_info_block_contains_phone_number_input(self, browser):
        block_contains_phone_number = BasketPage(browser)
        with allure.step('Открываем страницу каталога'):
            block_contains_phone_number.open_catalog()
        with allure.step('Нажимаем "Добавить в корзину" у карточки товара'):
            block_contains_phone_number.button_click_cards()
        with allure.step('Ждем пока товар добавится в корзину'):
            block_contains_phone_number.wait_for_element(basket_count)
        with allure.step('Нажимаем на иконку корзины'):
            block_contains_phone_number.sale_basket_click()
        with allure.step('Проверяем отображение поля Номер телефона'):
            assert block_contains_phone_number.get_input_phone_number() == INPUT_PHONE_NUMBER

    @allure.title('В блоке "Контактные данные" отображается инпут "E-mail"')
    def test_contact_info_block_contains_mail_input(self, browser):
        block_contains_mail = BasketPage(browser)
        with allure.step('Открываем страницу каталога'):
            block_contains_mail.open_catalog()
        with allure.step('Нажимаем "Добавить в корзину" у карточки товара'):
            block_contains_mail.button_click_cards()
        with allure.step('Ждем пока товар добавится в корзину'):
            block_contains_mail.wait_for_element(basket_count)
        with allure.step('Нажимаем на иконку корзины'):
            block_contains_mail.sale_basket_click()
        with allure.step('Проверяем отображение поля Номер E-mail'):
            assert block_contains_mail.get_input_mail() == INPUT_MAIL

    @allure.title('В блоке "Контактные данные" отображается инпут "Ваш комментарий"')
    def test_contact_info_block_contains_your_comment_input(self, browser):
        block_contains_your_comment = BasketPage(browser)
        with allure.step('Открываем страницу каталога'):
            block_contains_your_comment.open_catalog()
        with allure.step('Нажимаем "Добавить в корзину" у карточки товара'):
            block_contains_your_comment.button_click_cards()
        with allure.step('Ждем пока товар добавится в корзину'):
            block_contains_your_comment.wait_for_element(basket_count)
        with allure.step('Нажимаем на иконку корзины'):
            block_contains_your_comment.sale_basket_click()
        with allure.step('Проверяем отображение поля Номер Ваш комментарий'):
            assert block_contains_your_comment.get_input_your_comment() == INPUT_YOUR_COMMENT
