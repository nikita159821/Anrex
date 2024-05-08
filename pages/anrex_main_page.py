from locators.main_page_locators import logo, city, popup_city, close, search, first_city, callback_link, hover_text, \
    title_back_call, text_back_call, input_name, input_phone, name_placeholder, phone_placeholder, name_error, \
    title_sale, button_send_application, popup_back_call, phone_error
from pages.base_page import BasePage
from tests.data import NAME, PHONE, PHONE_NEGATIVE


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Получаем, сохраняем и возвращаем ссылку на img
    def get_logo_src(self):
        logo_element = self.find_element(*logo)
        logo_src = logo_element.get_attribute('src')
        return logo_src

    # Нажимаем на лого
    def logo_click(self):
        self.find_element(*logo).click()

    # Возвращает выбарнный город на странице
    def city_wrap(self):
        city_wrap = self.find_element(*city)
        return city_wrap

    # Нажимает на город на сайте
    def city_wrap_click(self):
        self.find_element(*city).click()

    # Возвращает тайтл "Выберите Ваш регион"
    def popup_city(self):
        popup = self.find_element(*popup_city)
        return popup

    # Нажимает на крестик в модальном окне выбора города
    def close_popup_click(self):
        self.find_element(*close).click()

    # Возвращает иконку поиска на главной странице  "Выберите Ваш регион"
    def search(self):
        search_ = self.find_element(*search).click()
        return search_

    # Находит первый город в модалке "Выберите Ваш регион"
    def first_sity(self):
        popup = self.find_element(*first_city)
        first_city_text = popup.text
        return first_city_text

    # Возвращает текст-ссылку "Заказать обратный звонок"
    def get_callback_link(self):
        link = self.find_element(*callback_link)
        return link

    # Нажимает на "Заказать обратный звонок"
    def click_callback_link(self):
        self.get_callback_link().click()

    # Метод находит элемент callback_link через метод get_callback_link,
    # наводит на него курсор и получает текст ховера из элемента hover_text.
    def get_hover_tooltip_text(self):
        hover = self.get_callback_link()
        self.actions.move_to_element(hover).perform()
        tooltip_text_element = self.find_element(*hover_text)
        tooltip_text = tooltip_text_element.text
        return tooltip_text

    # Возвращает тайтл "Заявка на обратный звонок"
    def get_back_call(self):
        title = self.find_element(*title_back_call)
        print(title.text)
        return self.remove_newline(title)

    # Возвращает текст в окне "Заявка на обратный звонок"
    def get_callback_popup_title(self):
        title = self.find_element(*text_back_call)
        return self.remove_newline(title)

    # Возвращает текст в окне "Заявка на обратный звонок" после оформления заявки
    def get_callback_title(self):
        title = self.find_element(*popup_back_call)
        return self.remove_newline(title)

    # Возвращает инпут "Ваше имя" в окне "Заявка на обратный звонок"
    def get_callback_popup_name_input(self):
        input_n = self.find_element(*input_name)
        return input_n

    # Возвращает инпут "Ваш телефон" в окне "Заявка на обратный звонок"
    def get_callback_popup_phone_input(self):
        input_p = self.find_element(*input_phone)
        return input_p

    # Возвращает плейсхолдер из поля "Ваше имя"
    def get_name_input_placeholder(self):
        input_placeholder_name = self.find_element(*name_placeholder)
        placeholder_value = input_placeholder_name.get_attribute("placeholder")
        return placeholder_value

    # Возвращает плейсхолдер из поля "Ваше имя"
    def get_phone_input_placeholder(self):
        input_placeholder_phone = self.find_element(*phone_placeholder)
        placeholder_value = input_placeholder_phone.get_attribute("placeholder")
        return placeholder_value

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
        error_div = self.find_element(*name_error)
        return error_div

    # Возвращает элемент с классом ошибки в поле "Ваш телефон"
    def phone_input_send_keys_error(self):
        error_div = self.find_element(*phone_error)
        return error_div

    # Возвращает тайтл "Товары со скидками"
    def get_title_sale(self):
        title_sale_text = self.find_element(*title_sale)
        return title_sale_text

    # Метод нажимает кнопку "Отправить заявку"
    def click_submit_application_button(self):
        self.find_element(*button_send_application).click()
