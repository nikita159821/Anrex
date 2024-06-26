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
    def body_send_keys(self, body):
        self.get_input_body().send_keys(body)

    @allure.step('Возвращает поле "Квартира"')
    def get_input_flat(self):
        return self.find(input_flat_send_keys)

    @allure.step('Вводит данные в поле "Квартира"')
    def flat_send_keys(self, flat):
        self.get_input_flat().send_keys(flat)

    @allure.step('Возвращает поле "Телефон"')
    def get_input_phone_number(self):
        return self.find(input_phone_number_send_keys)

    @allure.step('Вводит данные в поле "Телефон"')
    def phone_number_send_keys(self, phone):
        self.get_input_phone_number().send_keys(phone)

    @allure.step('Возвращает поле "Email"')
    def get_input_mail(self):
        return self.find(input_mail_send_keys)

    @allure.step('Вводит данные в поле "Email"')
    def mail_send_keys(self, mail):
        self.get_input_mail().send_keys(mail)

    @allure.step('Возвращает поле "Комментарий"')
    def get_input_your_comment(self):
        return self.find(input_your_comment_send_keys)

    @allure.step('Вводит данные в поле "Комментарий"')
    def your_comment_send_keys(self, comment):
        self.get_input_your_comment().send_keys(comment)

    @allure.step('Вводит данные в поля')
    def fill_form(self, name=None, city=None, street=None, house=None, flat=None, body=None, phone=None, mail=None,
                  comment=None):
        if name:
            self.name_input_send_keys(name)
        if city:
            self.delivery_city_send_keys(city)
        if street:
            self.street_send_keys(street)
        if house:
            self.house_send_keys(house)
        if flat:
            self.flat_send_keys(flat)
        if body:
            self.body_send_keys(body)
        if phone:
            self.phone_number_send_keys(phone)
        if mail:
            self.mail_send_keys(mail)
        if comment:
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

    @allure.step('Возвращает текст ошибки поля "Номер телефона".')
    def get_text_error_phone(self):
        return self.get_text_of_element(error_phone)

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

    @allure.step('Ожидает текст ошибки поля "Номер телефона"')
    def wait_for_error_phone(self):
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(error_phone)
        )

    @allure.title('Возвращает количество товаров в корзине')
    def get_text_count_products_basket(self):
        return self.get_text_of_element(count_products_basket)

    @allure.title('Возвращает текст хлебной крошки "Главная"')
    def get_text_home_breadcrumb(self):
        return self.get_text_of_element(home_breadcrumb)

    @allure.title('Возвращает текст хлебной крошки "Корзина"')
    def get_text_basket_breadcrumb(self):
        return self.get_text_of_element(basket_breadcrumb)

    @allure.title('Нажимает на текст хлебной крошки "Корзина"')
    def click_basket_breadcrumb(self):
        self.click_element(basket_breadcrumb)

    @allure.title('Нажимает на текст хлебной крошки "Главная"')
    def click_home_breadcrumb(self):
        self.click_element(home_breadcrumb)

    @allure.title('Возвращает фото карточки товара')
    def get_img_products_card(self):
        return self.find(image_card)

    @allure.title('Возвращает название товара в корзине')
    def get_text_name_products_basket(self):
        return self.get_text_of_element(name_card_basket)

    @allure.title('Возвращает название товара в каталоге')
    def get_text_name_products_catalog(self):
        return self.get_text_of_element(name_card_catalog)

    @allure.title('Возвращает кнопку добавления товара в корзине "+"')
    def get_plus_button(self):
        return self.find(plus_button_basket)

    @allure.title('Возвращает кнопку уменьшения количества товаров в корзине "-"')
    def get_decrease_item_quantity(self):
        return self.find(decrease_item_quantity)

    @allure.title('Возвращает кнопку удаления товара в корзине')
    def get_remove_product_button(self):
        return self.find(remove_product_button)

    @allure.title('Возвращает название коллекции товара в каталоге')
    def get_text_collection_products_catalog(self):
        return self.get_text_of_element(catalog_collection)

    @allure.title('Возвращает название коллекции товара в корзине')
    def get_text_collection_products_basket(self):
        return self.get_text_of_element(basket_collection)

    @allure.title('Нажимает на название товара в корзине')
    def click_name_card_basket(self):
        return self.click_element(name_card_basket)

    @allure.title('Возвращает ссылку товара в корзине')
    def get_url_products_basket(self):
        return self.get_attribute_of_element(name_card_url, 'href')

    @allure.title('Нажимает кнопку добавления товара в корзине "+"')
    def click_plus_button(self):
        self.click_element(plus_button_basket)

    @allure.title('Нажимает кнопку уменьшения количества товаров в корзине "-"')
    def click_decrease_item_quantity(self):
        self.click_element(decrease_item_quantity)

    @allure.title('Возвращает количество товаров из счетчика в корзине')
    def get_text_input_count_basket(self):
        element = self.find(input_count_basket)
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located(input_count_basket))
        return element.get_attribute('value')

    @allure.title('Вводит количество товаров в инпут счётчика в корзине')
    def send_keys_input_count_basket(self, text):
        self.send_keys_text_of_element(input_count_basket, text)

    @allure.title('Возвращает тайтл "Ваша корзина"')
    def get_text_title_basket(self):
        return self.get_text_of_element(title_basket)

    @allure.title('Возвращает текст "Вы еще не добавили ни одного товара в Вашу корзину"')
    def get_text_basket(self):
        return self.get_text_of_element(text_basket)

    @allure.title('Нажимает кнопку "Начать покупки"')
    def click_button_shopping(self):
        self.click_element(button_shopping)

    @allure.title('Возвращает кнопку "Начать покупки"')
    def get_button_shopping(self):
        return self.find(button_shopping)

    @allure.title('Возвращает способ оплаты "Наличными при получении*"')
    def get_text_payment_in_cash(self):
        return self.get_text_of_element(payment_in_cash)

    @allure.title('Возвращает способ оплаты "Банковской картой"')
    def get_text_payment_bank_card(self):
        return self.get_text_of_element(payment_bank_card)

    @allure.title('Возвращает способ оплаты "Рассрочка от Тинькофф"')
    def get_text_payment_installment(self):
        return self.get_text_of_element(payment_installment)

    @allure.title('Возвращает способ оплаты "Частями с Яндекс Сплит"')
    def get_text_payment_yandex_split(self):
        return self.get_text_of_element(payment_yandex_split)

    @allure.title('Возвращает поле для ввода промокода')
    def remove_focus_from_input_count(self):
        return self.find(promo_code_input).click()


