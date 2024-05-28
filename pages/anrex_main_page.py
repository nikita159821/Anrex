from selenium.webdriver import ActionChains

from locators.main_page_locators import *
from pages.base_page import BasePage
from tests.data import NAME, PHONE, PHONE_NEGATIVE, COMMENT


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
        return self.get_text_of_element(popup_city)

    # Нажимает на крестик в модальном окне выбора города
    def close_popup_click(self):
        self.click_element(close)

    # Возвращает иконку поиска на главной странице "Выберите Ваш регион"
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
        return self.remove_newline(title_back_call)

    # Возвращает текст в окне "Заявка на обратный звонок"
    def get_callback_popup_title(self):
        return self.remove_newline(text_back_call)

    # Возвращает текст в окне "Заявка на обратный звонок" после оформления заявки
    def get_callback_title(self):
        return self.remove_newline(popup_back_call)

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

    # Модифицированный метод для ввода текста в поле "Ваше имя" в форме обратный звонок
    def t_name_input_send_keys(self, name):
        self.get_callback_popup_name_input().send_keys(name)

    # Модифицированный метод для ввода текста в поле "Ваше имя" в форме обратной связи
    def form_name_input_send_keys(self, name):
         self.get_form_feedback_name_input().send_keys(name)

    # Модифицированный метод для ввода текста в поле "Ваш телефон" в форме обратной связи
    def form_phone_input_send_keys(self, phone):
        self.get_form_feedback_phone_input().send_keys(phone)

    # Модифицированный метод для ввода текста в поле "Ваша почта" в форме обратной связи
    def form_email_input_send_keys(self, email):
        self.get_form_feedback_email_input().send_keys(email)

    # Модифицированный метод для ввода номера телефон в поле "Ваш телефон"
    def t_phone_input_send_keys(self, phone, input_locator):
        phone_input = self.find_element(*input_locator)
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
        input_element = self.find_element(*name_error)
        class_attribute = input_element.get_attribute('class')
        return class_attribute

    # Возвращает элемент с классом ошибки в поле "Ваш телефон"
    def phone_input_send_keys_error(self):
        input_element = self.find_element(*phone_error)
        class_attribute = input_element.get_attribute('class')
        return class_attribute

    # Возвращает элемент с классом ошибки в поле "Ваш телефон"
    def email_input_send_keys_error(self):
        input_element = self.find_element(*email_error)
        class_attribute = input_element.get_attribute('class')
        return class_attribute

    # Возвращает тайтл "Товары со скидками"
    def get_title_sale(self):
        return self.get_text_of_element(title_sale)

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

    # Возвращает элемент после закрытия строки поиска
    def get_search_input_close(self):
        return self.find_element(*search_line_close)

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
        count_text = self.get_attribute_of_element(basket_count, 'textContent')
        # Удалить скобки из текста счетчика
        count_text = count_text.replace('(', '').replace(')', '')
        return count_text

    # Возвращает текст раздела "Каталог" в шапке сайта
    def get_catalog_text(self):
        return self.get_text_of_element(catalog)

    # Возвращает раздел "Каталог" в шапке сайта
    def get_catalog(self):
        return self.browser.find_element(*catalog)

    # Возвращает список каталога "по типу мебели" и "По комнате"
    #def get_type_of_furniture_and_room(self):
    #return self.get_elements_text(by_type_of_furniture_and_room)

    # Нажимает на раздел "Тумбы"
    def click_tumby(self):
        self.click_element(tumby)

    # Нажимает на раздел "Смотреть всё"
    def click_see_all(self):
        self.click_element(see_all)

    # Возвращает текст раздела "Коллекци" в шапке сайта
    def get_collections_text(self):
        return self.get_text_of_element(collections)

    # Нажимает на раздел "Коллекци"
    def click_collections(self):
        self.click_element(collections)

    # Возвращает раздел "Покупателям" в шапке сайта
    def get_cdelivery(self):
        return self.browser.find_element(*delivery)

    # Возвращает текст раздела "Покупателям" в шапке сайта
    def get_cdelivery_text(self):
        return self.get_text_of_element(delivery)

    # Нажимает на раздел "Покупателям"
    def click_delivery(self):
        self.click_element(delivery)

    # Нажимает на раздел "Доставка и сборка" в выпадающем списке
    def click_delivery_dropdown(self):
        self.click_element(delivery_dropdown)

    # Нажимает на раздел "Адреса магазинов" в выпадающем списке
    def click_shops_dropdown(self):
        self.click_element(shops)

    # Нажимает на раздел "Гарантия на мебель" в выпадающем списке
    def click_guarantee_dropdown(self):
        self.click_element(guarantee)

    # Возвращает текст раздела "Скидки" в шапке сайта
    def get_sale_text(self):
        return self.get_text_of_element(sale)

    # Нажимает на раздел "Скидки"
    def click_sale(self):
        self.click_element(sale)

    # Возвращает текст раздела "Каталог" в шапке сайта
    def get_about_text(self):
        return self.get_text_of_element(about)

    # Нажимает на раздел "О компании"
    def click_about(self):
        self.click_element(about)

    # Нажимает на раздел "Информация о компании" в выпадающем списке
    def click_about_dropdown(self):
        self.click_element(about_dropdown)

    # Нажимает на раздел "Информация о компании" в выпадающем списке
    def click_dealers_dropdown(self):
        self.click_element(dealers_dropdown)

    # Нажимает на раздел "Информация о компании" в выпадающем списке
    def click_contact_dropdown(self):
        self.click_element(contact_dropdown)

    # Скролл до блока "Товары со скидками"
    def scroll_to_element(self, element):
        actions = ActionChains(self.browser)
        actions.move_to_element(element).perform()

    # Возвращает блок "Товары со скидками"
    def get_discounted_products(self):
        return self.find(discounted_products)

    # Возвращает блок "Популярные категории"
    def get_popular_categories(self):
        return self.get_element_scroll_to_element(popular_categories)

    # Скролл до блока "Популярные категории"
    def scroll_to_popular_categories(self, element):
        actions = ActionChains(self.browser)
        actions.move_to_element(element).perform()

    # Нажимает на "Кровати и матрасы" в блоке "Популярные категории"
    def click_popular_categories(self):
        self.click_element(popular_section_banner)

    # Возвращает слайдер с разделами на главной
    def get_slider(self):
        return self.get_element_scroll_to_element(banner_slider)

    # Нажимает кнопку вверх на слайдере разделов
    def click_up_slider(self):
        self.click_element(button_up)

    # Нажимает кнопку вверх на слайдере разделов
    def click_down_slider(self):
        self.click_element(button_down)

    # Возвращает текст раздела на слайдере "Гостиных"
    def get_text_slider_living_rooms(self):
        return self.get_text_of_element(slider_gostinie)

    # Возвращает текст раздела на слайдере "Кабинетов"
    def get_text_slider_cabinets(self):
        return self.get_text_of_element(slider_gostinie)

    # Возвращает текст "Мебель для" из слайдера разделов
    def get_text_slider_title(self):
        return self.get_text_of_element(carousel_title)

    # Возвращает изображение на слейдере разделов
    def get_slider_img(self):
        return self.get_attribute_of_element(img, 'src')

    # Возвращает блок "Наши коллекции"
    def get_section_collections(self):
        return self.get_element_scroll_to_element(section_collections)

    # Нажимает стрелку вправо в разделе "Наши коллекции"
    def click_button_right(self):
        self.click_element(button_right)

    # Нажимает стрелку влево в разделе "Наши коллекции"
    def click_button_left(self):
        self.click_element(button_left)

    # Возвращает название коллекции "Джаз"
    def collections_title_jazz(self):
        return self.get_text_of_element(collections_title_jazz)

    # Возвращает название коллекции "Валенсия"
    def collections_title_valencia(self):
        return self.get_text_of_element(collections_title_valencia)

    # Возвращает текст кнопки "Смотреть коллекцию"
    def get_button_text_collections(self):
        return self.get_text_of_element(button_collections)

    # Возвращает кнопку "Смотреть коллекцию"
    def get_click_button_collections(self):
        self.click_element(button_collections)

    # Возвращает текст кнопки "Смотреть все коллекции"
    def get_button_text_view_collections(self):
        return self.get_text_of_element(view_collections)

    # Возвращает кнопку "Смотреть все коллекции"
    def get_click_button_view_collections(self):
        self.click_element(view_collections)

    # Возвращает блок "Отзывы наших покупателей"
    def get_section_reviews(self):
        return self.get_element_scroll_to_element(reviews)

    # Возвращает блок футера
    def get_section_footer(self):
        return self.get_element_scroll_to_element(footer)

    # Возвращает список элементов "Отзывы наших покупателей"
    def get_sections_reviews(self):
        return self.find_elements(*review_cards)

    # Возвращаем словарь с данными отзыва
    def get_review_data(self):
        name_text = self.get_text_of_element(name)
        date_text = self.get_text_of_element(date)
        content_text = self.get_text_of_element(content)
        return {
            'name': name_text,
            'date': date_text,
            'content': content_text
        }

    # Возвращает рейтинг в отзывах
    def get_review_stars(self):
        return self.find_element(*stars)

    # Возвращает текст кнопки "Читать отзыв полностью"
    def get_read_more_link_text(self):
        return self.get_text_of_element(read_more_link)

    # Возвращает кнопку "Читать отзыв полностью"
    def get_read_more_link_click(self):
        self.click_element(read_more_link)

    # Возвращает модально окно с отзывом
    def get_review_popup(self):
        return self.find_element(*review_popup)

    # Нажимает кнопку закрытия модального окна с отзывом
    def click_popup_close_review(self):
        self.click_element(popup_close_review)

    # Возвращает текст кнопки "Смотреть все отзывы"
    def get_text_button_review(self):
        return self.get_text_of_element(review_button)

    # Возвращает кнопку "Смотреть все отзывы"
    def button_review_click(self):
        self.click_element(review_button)

    # Получаем, сохраняем и возвращаем ссылку на img в футере
    def get_logo_footer_src(self):
        return self.get_attribute_of_element(logo_footer, 'src')

    # Возвращает наименование организации в футере
    def get_text_footer(self):
        return self.get_text_of_element(name_of_company)

    # Возвращает информацию для покупателя в футере
    def get_text_comment(self):
        return self.get_text_of_element(text_comment)

    # Возвращает текст кнопки "Написать нам"
    def get_text_button_write(self):
        return self.get_text_of_element(button_write)

    # Нажимает кнопку "Написать нам"
    def click_button_write(self):
        self.click_element(button_write)

    # Возвращает тайтл "Форма обратной связи"
    def get_title_form_feedback(self):
        return self.get_text_of_element(title_form_feedback)

    # Возвращает текст в форме обратной связи
    def get_text_form_feedback(self):
        return self.remove_newline(text_form_feedback)

    # Возвращает текст радиокнопок в форме обратной связи
    def get_text_radio_buttons(self):
        return self.get_elements_text_form(radio_buttons)

    # Закрыват форму обратной связи через крестик
    def click_form_close(self):
        self.click_element(form_close)

    # Возвращает поле "Ваше имя" в форме обратной связи
    def get_form_feedback_name_input(self):
        return self.find_element(*input_name_form_feedback)

    # Возвращает поле "Ваш телефон" в форме обратной связи
    def get_form_feedback_phone_input(self):
        return self.find_element(*input_phone_form_feedback)

    # Возвращает поле "Ваша почта" в форме обратной связи
    def get_form_feedback_email_input(self):
        return self.find_element(*input_email_form_feedback)

    # Возвращает поле "Ваш вопрос/комментарий" в форме обратной связи
    def get_form_feedback_question_input(self):
        return self.find_element(*question_placeholder_form_feedback)

    # Возвращает плейсхолдер из поля "Ваше имя", в форме обратной связи
    def get_placeholder_form_feedback_name_input(self):
        return self.get_attribute_of_element(name_placeholder_form_feedback, 'placeholder')

    # Возвращает плейсхолдер из поля "Ваш телефон", в форме обратной связи
    def get_placeholder_form_feedback_phone_input(self):
        return self.get_attribute_of_element(phone_placeholder_form_feedback, 'placeholder')

    # Возвращает плейсхолдер из поля "Ваша почта", в форме обратной связи
    def get_placeholder_form_feedback_email_input(self):
        return self.get_attribute_of_element(email_placeholder_form_feedback, 'placeholder')

    # Возвращает плейсхолдер из поля "Введите Ваш комментарий", в форме обратной связи
    def get_placeholder_form_question_input(self):
        return self.get_attribute_of_element(question_placeholder_form_feedback, 'placeholder')

    # Возвращает кнопку "Отправить форму" в форме обратной связи
    def get_button_form_feedback(self):
        return self.find_element(*button_form_feedback)

    # Нажимает первую радиокнопку в форме обратной связи
    def click_checkbox_radio_button(self):
        self.click_element(checkbox_radio_button)

    def text_popup_form_feedback(self):
        return self.remove_newline(popup_form_feedback)

    # Вводит данные в поле "Введите Ваш комментарий" в форме обратной связи
    def send_keys_input_question_form_feedback(self):
        self.get_form_feedback_question_input().send_keys(COMMENT)

    # Вводит данные в поле "Ваш телефон" в форме обратной связи
    def send_keys_input_phone_form_feedback(self):
        self.get_form_feedback_phone_input().send_keys(PHONE)

    # Нажимает кнопку "Отправить форму" в форме обратной связи
    def click_button_form_feedback(self):
        self.click_element(button_form_feedback)

    # Удаляем данные из поля "Ваш телефон"
    def phone_input_delete_form_feedback(self):
        self.get_form_feedback_phone_input().clear()

    # Вводим в поле "Ваш телефон" 12 цифр в форме обратной связи
    def send_keys_12_digits_form_feedback_phone_input(self):
        self.get_form_feedback_phone_input().send_keys(PHONE_NEGATIVE)