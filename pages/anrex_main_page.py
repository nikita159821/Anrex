from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains

from locators.main_page_locators import *
from pages.base_page import BasePage
from tests.data import NAME, PHONE, PHONE_NEGATIVE


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Получаем, сохраняем и возвращаем ссылку на img
    def get_logo_src(self):
        return self.get_attribute_of_element(logo, 'src')

    # Нажимаем на лого
    def logo_click(self):
        self.click_element(logo)

    # Возвращает выбранный город на странице
    def city_wrap(self):
        return self.find_element(*city)

    # Нажимает на город на сайте
    def city_wrap_click(self):
        self.click_element(city)

    # Возвращает тайтл "Выберите Ваш регион"
    def popup_city(self):
        return self.find_element(*popup_city)

    # Нажимает на крестик в модальном окне выбора города
    def close_popup_click(self):
        self.click_element(close)

    # Возвращает иконку поиска на главной странице  "Выберите Ваш регион"
    def search(self):
        self.click_element(search)

    # Находит первый город в модалке "Выберите Ваш регион"
    def first_sity(self):
        return self.get_text_of_element(first_city)

    # Возвращает текст-ссылку "Заказать обратный звонок"
    def get_callback_link(self):
        return self.find_element(*callback_link)

    # Нажимает на "Заказать обратный звонок"
    def click_callback_link(self):
        self.click_element(callback_link)

    # Метод находит элемент callback_link через метод get_callback_link,
    # наводит на него курсор и получает текст ховера из элемента hover_text.
    def get_hover_tooltip_text(self):
        hover = self.get_callback_link()
        self.actions.move_to_element(hover).perform()
        return self.get_text_of_element(hover_text)

    # Возвращает тайтл "Заявка на обратный звонок"
    def get_back_call(self):
        title = self.find_element(*title_back_call)
        return self.remove_newline(title)

    # Возвращает текст в окне "Заявка на обратный звонок"
    def get_callback_popup_title(self):
        title = self.find_element(*text_back_call)
        return self.remove_newline(title)

    # Возвращает текст в окне "Заявка на обратный звонок" после оформления заявки
    def get_callback_title(self):
        title = self.find_element(*popup_back_call)
        return self.remove_newline(title)

    # Возвращает объект веб-элемента "Заявка на обратный звонок"
    def get_callback_title_element(self):
        return self.find_element(*popup_back_call)

    # Возвращает инпут "Ваше имя" в окне "Заявка на обратный звонок"
    def get_callback_popup_name_input(self):
        return self.find_element(*input_name)

    # Возвращает инпут "Ваш телефон" в окне "Заявка на обратный звонок"
    def get_callback_popup_phone_input(self):
        return self.find_element(*input_phone)

    # Возвращает плейсхолдер из поля "Ваше имя"
    def get_name_input_placeholder(self):
        return self.get_attribute_of_element(name_placeholder, 'placeholder')

    # Возвращает плейсхолдер из поля "Ваше имя"
    def get_phone_input_placeholder(self):
        return self.get_attribute_of_element(phone_placeholder, 'placeholder')

    # Вводим в поле "Ваше имя" одну букву
    def name_input_send_keys(self):
        self.get_callback_popup_name_input().send_keys(NAME)

    # Вводим в поле "Ваше имя" пробел
    def name_input_send_keys_spaces(self):
        self.get_callback_popup_name_input().send_keys(" ")

    # Удаляем данные из поля "Ваше имя"
    def name_input_delete(self):
        self.get_callback_popup_name_input().clear()

    # Модифицированный метод для ввода текста в поле "Ваше имя"
    def t_name_input_send_keys(self, name):
        name_input = self.get_callback_popup_name_input()
        name_input.send_keys(name)

    # Модифицированный метод для ввода номера телефон в поле "Ваш телефон"
    def t_phone_input_send_keys(self, phone):
        phone_input = self.get_callback_popup_phone_input()
        phone_input.send_keys(phone)

    # Вводим в поле "Ваш телефон"
    def phone_input_send_keys(self):
        self.get_callback_popup_phone_input().send_keys(PHONE)

    # Вводим в поле "Ваш телефон" 12 цифр
    def send_keys_12_digits_to_phone_input(self):
        self.get_callback_popup_phone_input().send_keys(PHONE_NEGATIVE)

    # Удаляем данные из поля "Ваш телефон"
    def phone_input_delete(self):
        self.get_callback_popup_phone_input().clear()

    # Возвращает элемент с классом ошибки в поле "Ваше имя"
    def name_input_send_keys_error(self):
        return self.find_element(*name_error)

    # Возвращает элемент с классом ошибки в поле "Ваш телефон"
    def phone_input_send_keys_error(self):
        return self.find_element(*phone_error)

    # Возвращает тайтл "Товары со скидками"
    def get_title_sale(self):
        return self.find_element(*title_sale)

    # Метод нажимает кнопку "Отправить заявку"
    def click_submit_application_button(self):
        self.click_element(button_send_application)

    # Возвращает номер телефона в шапке
    def get_phone_callback(self):
        return self.get_text_of_element(tel_callback)

    # Возвращает svg иконки поиска в шапке сайта
    def get_search_cvg(self):
        return self.get_attribute_of_element(search_cvg, 'xmlns')

    # Нажимает иконку поиска в шапке сайта
    def get_search_click(self):
        self.click_element(search)

    def get_search_active(self):
        self.click_element(search_active)

    # Возвращает строку поиска
    def get_search_input(self):
        return self.find_element(*search_line)

    # Возвращает иконку корзины
    def get_sale_basket(self):
        return self.find_element(*sale_basket)

    # Нажимает на иконку корзины в шапке
    def sale_basket_click(self):
        self.click_element(sale_basket)

    # Нажимает "Добавить в корзину" у карточки товара
    def button_click_cards(self):
        button = self.find_element(*button_card)
        self.scroll_to_element_and_click(button)

    # Скролл до карточки товара
    def scroll_to_element_and_click(self, element):
        actions = ActionChains(self.browser)
        actions.move_to_element(element).perform()
        element.click()

    # Возвращает количество добавленных товаров в корзину
    def basket_count(self):
        return self.get_attribute_of_element(basket_count, 'textContent')

    # Возвращает текст раздела "Каталог" в шапке сайта
    def get_catalog_text(self):
        return self.get_text_of_element(catalog)

    # Возвращает раздел "Каталог" в шапке сайта
    def get_catalog(self):
        return self.browser.find_element(*catalog)

    # Возвращает список каталога "по типу мебели" и "По комнате"
    def get_type_of_furniture_and_room(self):
        return self.get_elements_text(by_type_of_furniture_and_room)
