import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.basket_page_locators import *
from pages.base_page import BasePage


class BasketPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Возвращает текст поле "ФИО"')
    def text_input_full_name(self):
        return self.get_text_of_element(input_full_name)

    @allure.step('Возвращает текст поле "Город доставки"')
    def text_input_delivery_city(self):
        return self.get_text_of_element(input_delivery_city)

    @allure.step('Возвращает текст поле "Улица"')
    def text_input_street(self):
        return self.get_text_of_element(input_street)

    @allure.step('Возвращает текст поле "Дом"')
    def text_input_house(self):
        return self.get_text_of_element(input_house)

    @allure.step('Возвращает текст поле "Корпус"')
    def text_input_body(self):
        return self.get_text_of_element(input_body)

    @allure.step('Возвращает текст поле "Квартира"')
    def text_input_flat(self):
        return self.get_text_of_element(input_flat)

    @allure.step('Возвращает текст поле "Номер телефона"')
    def text_input_phone_number(self):
        return self.get_text_of_element(input_phone_number)

    @allure.step('Возвращает текст поле "E-mail"')
    def text_input_mail(self):
        return self.get_text_of_element(input_mail)

    @allure.step('Возвращает текст поле "Ваш комментарий"')
    def text_input_your_comment(self):
        return self.get_text_of_element(input_your_comment)

    @allure.step('Возвращает плейсхолдер из поля "Ваше имя"')
    def get_input_name_placeholder(self):
        return self.get_attribute_of_element(placeholder_name, 'placeholder')

    @allure.step('Возвращает плейсхолдер из поля "Адрес"')
    def get_input_address_placeholder(self):
        return self.get_attribute_of_element(placeholder_address, 'placeholder')

    @allure.step('Возвращает плейсхолдер из поля "Улица"')
    def get_input_street_placeholder(self):
        return self.get_attribute_of_element(placeholder_street, 'placeholder')

    @allure.step('Возвращает плейсхолдер из поля "Дом"')
    def get_input_house_placeholder(self):
        return self.get_attribute_of_element(placeholder_house, 'placeholder')

    @allure.step('Возвращает плейсхолдер из поля "Корпус"')
    def get_input_building_placeholder(self):
        return self.get_attribute_of_element(placeholder_building, 'placeholder')

    @allure.step('Возвращает плейсхолдер из поля "Квартира"')
    def get_input_apartment_placeholder(self):
        return self.get_attribute_of_element(placeholder_apartment, 'placeholder')

    @allure.step('Возвращает плейсхолдер из поля "Номер телефона"')
    def get_input_phone_placeholder(self):
        return self.get_attribute_of_element(placeholder_phone, 'placeholder')

    @allure.step('Возвращает плейсхолдер из поля "E-mail"')
    def get_input_email_placeholder(self):
        return self.get_attribute_of_element(placeholder_email, 'placeholder')

    @allure.step('Возвращает плейсхолдер из поля "Ваш комментарий"')
    def get_input_comment_placeholder(self):
        return self.get_attribute_of_element(placeholder_comment, 'placeholder')

    @allure.step('Возвращает поле "ФИО"')
    def get_input_full_name(self):
        return self.find(name_input_send_keys)

    @allure.step('Вводит данные в поле "ФИО"')
    def name_input_send_keys(self, name):
        self.get_input_full_name().send_keys(name)

    @allure.step('Возвращает поле "Город доставки"')
    def get_input_delivery_city(self):
        return self.find(input_delivery_city_send_keys)

    @allure.step('Вводит данные в поле "Город доставки"')
    def delivery_city_send_keys(self, city):
        self.get_input_delivery_city().send_keys(city)

    @allure.step('Возвращает поле "Улица"')
    def get_input_street(self):
        return self.find(input_street_send_keys)

    @allure.step('Вводит данные в поле "Улица"')
    def street_send_keys(self, street):
        self.get_input_street().send_keys(street)

    @allure.step('Возвращает поле "Дом"')
    def get_input_house(self):
        return self.find(input_house_send_keys)

    @allure.step('Вводит данные в поле "Дом"')
    def house_send_keys(self, house):
        self.get_input_house().send_keys(house)

    @allure.step('Возвращает поле "Корпус"')
    def get_input_body(self):
        return self.find(input_body_send_keys)

    @allure.step('Вводит данные в поле "Корпус"')
    def body_send_keys(self,body):
        self.get_input_body().send_keys(body)

    @allure.step('Возвращает поле "Квартира"')
    def get_input_flat(self):
        return self.find(input_flat_send_keys)

    @allure.step('Вводит данные в поле "Квартира"')
    def flat_send_keys(self,flat):
        self.get_input_flat().send_keys(flat)

    @allure.step('Возвращает поле "Телефон"')
    def get_input_phone_number(self):
        return self.find(input_phone_number_send_keys)

    @allure.step('Вводит данные в поле "Телефон"')
    def phone_number_send_keys(self,phone):
        self.get_input_phone_number().send_keys(phone)

    @allure.step('Возвращает поле "Email"')
    def get_input_mail(self):
        return self.find(input_mail_send_keys)

    @allure.step('Вводит данные в поле "Email"')
    def mail_send_keys(self,mail):
        self.get_input_mail().send_keys(mail)

    @allure.step('Возвращает поле "Комментарий"')
    def get_input_your_comment(self):
        return self.find(input_your_comment_send_keys)

    @allure.step('Вводит данные в поле "Комментарий"')
    def your_comment_send_keys(self,comment):
        self.get_input_your_comment().send_keys(comment)

    @allure.step('Вводит данные в поля')
    def fill_form(self, name, city, street, house, body, flat, phone, mail, comment):
        with allure.step('Заполняем поле "Ваше имя" данными'):
            self.name_input_send_keys(name)
        with allure.step('Заполняем поле "Город доставки" данными'):
            self.delivery_city_send_keys(city)
        with allure.step('Заполняем поле "Улица" данными'):
            self.street_send_keys(street)
        with allure.step('Заполняем поле "Дом" данными'):
            self.house_send_keys(house)
        with allure.step('Заполняем поле "Корпус" данными'):
            self.body_send_keys(body)
        with allure.step('Заполняем поле "Квартира" данными'):
            self.flat_send_keys(flat)
        with allure.step('Заполняем поле "Телефон" данными'):
            self.phone_number_send_keys(phone)
        with allure.step('Заполняем поле "Email" данными'):
            self.mail_send_keys(mail)
        with allure.step('Заполняем поле "Комментарий" данными'):
            self.your_comment_send_keys(comment)

    @allure.step('Нажимает кнопку "Оформить заказ" в корзине')
    def click_button_arrange_order(self):
        self.click_element(button_arrange_order)

    @allure.step('Возвращает текст "Подтверждение заказа"')
    def get_text_order_confirmation(self):
        return self.get_text_of_element(order_confirmation)

    @allure.step('Ожидает видимость текста "Подтверждение заказа"')
    def wait_for_order_confirmation(self):
        return WebDriverWait(self.browser, 50).until(
            EC.visibility_of_element_located(order_confirmation)
        )

    @allure.step('Возвращает текст ошибки поля "Ваше имя".')
    def get_text_error_name(self):
        return self.get_text_of_element(error_name)

    @allure.step('Возвращает текст ошибки поля "Город доставки".')
    def get_text_error_city(self):
        return self.get_text_of_element(error_city)

    @allure.step('Возвращает текст ошибки поля "Улица".')
    def get_text_error_street(self):
        return self.get_text_of_element(error_street)

    @allure.step('Возвращает текст ошибки поля "Дом".')
    def get_text_error_house(self):
        return self.get_text_of_element(error_house)

    @allure.step('Возвращает текст ошибки поля "E-mail".')
    def get_text_error_email(self):
        return self.get_text_of_element(error_email)

    @allure.step('Ожидает текст ошибки поля "Ваше имя"')
    def wait_for_error_name(self):
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(error_name)
        )

    @allure.step('Ожидает текст ошибки поля "Город доставки"')
    def wait_for_error_city(self):
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(error_city)
        )

    @allure.step('Ожидает текст ошибки поля "Улица"')
    def wait_for_error_street(self):
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(error_street)
        )

    @allure.step('Ожидает текст ошибки поля "Дом"')
    def wait_for_error_house(self):
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(error_house)
        )

    @allure.step('Ожидает текст ошибки поля "E-mail"')
    def wait_for_error_email(self):
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(error_email)
        )
