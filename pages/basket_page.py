import allure
from locators.basket_page_locators import *
from pages.base_page import BasePage


class BasketPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Возвращает поле ФИО')
    def get_input_full_name(self):
        return self.get_text_of_element(input_full_name)

    @allure.step('Возвращает поле Город доставки')
    def get_input_delivery_city(self):
        return self.get_text_of_element(input_delivery_city)

    @allure.step('Возвращает поле Улица')
    def get_input_street(self):
        return self.get_text_of_element(input_street)

    @allure.step('Возвращает поле Дом')
    def get_input_house(self):
        return self.get_text_of_element(input_house)

    @allure.step('Возвращает поле Корпус')
    def get_input_body(self):
        return self.get_text_of_element(input_body)

    @allure.step('Возвращает поле Квартира')
    def get_input_flat(self):
        return self.get_text_of_element(input_flat)

    @allure.step('Возвращает поле Номер телефона')
    def get_input_phone_number(self):
        return self.get_text_of_element(input_phone_number)

    @allure.step('Возвращает поле E-mail')
    def get_input_mail(self):
        return self.get_text_of_element(input_mail)

    @allure.step('Возвращает поле Ваш комментарий')
    def get_input_your_comment(self):
        return self.get_text_of_element(input_your_comment)

    @allure.step('Возвращает плейсхолдер из поля Ваше имя')
    def get_input_name_placeholder(self):
        return self.get_attribute_of_element(placeholder_name, 'placeholder')

    @allure.step('Возвращает плейсхолдер из поля Адрес')
    def get_input_address_placeholder(self):
        return self.get_attribute_of_element(placeholder_address, 'placeholder')

    @allure.step('Возвращает плейсхолдер из поля Улица')
    def get_input_street_placeholder(self):
        return self.get_attribute_of_element(placeholder_street, 'placeholder')

    @allure.step('Возвращает плейсхолдер из поля Дом')
    def get_input_house_placeholder(self):
        return self.get_attribute_of_element(placeholder_house, 'placeholder')

    @allure.step('Возвращает плейсхолдер из поля Корпус')
    def get_input_building_placeholder(self):
        return self.get_attribute_of_element(placeholder_building, 'placeholder')

    @allure.step('Возвращает плейсхолдер из поля Квартира')
    def get_input_apartment_placeholder(self):
        return self.get_attribute_of_element(placeholder_apartment, 'placeholder')

    @allure.step('Возвращает плейсхолдер из поля Номер телефона')
    def get_input_phone_placeholder(self):
        return self.get_attribute_of_element(placeholder_phone, 'placeholder')

    @allure.step('Возвращает плейсхолдер из поля E-mail')
    def get_input_email_placeholder(self):
        return self.get_attribute_of_element(placeholder_email, 'placeholder')

    @allure.step('Возвращает плейсхолдер из поля Ваш комментарий')
    def get_input_comment_placeholder(self):
        return self.get_attribute_of_element(placeholder_comment, 'placeholder')



