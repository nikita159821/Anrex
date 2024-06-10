import random
import string

import allure
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import slider, button_card, sale_basket, basket_count
from tests_main_page.data import RUSSIAN_LETTERS, PUNCTUATION
from tests_main_page.urls import URL, CHAPTER_CATALOG


# Класс для кастомного условия ожидания
class element_to_be:
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        driver.find_element(*self.locator)  # Находим элемент


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.actions = ActionChains(self.browser)

    def wait(self, locator):
        WebDriverWait(self.browser, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.browser.find_element(*locator)

    def find_element(self, *args):
        return self.browser.find_element(*args)

    def find_elements(self, *args):
        return self.browser.find_elements(*args)

    # Общий метод для поиска элемента
    def find(self, locator):
        return self.find_element(*locator)

    # Общий метод для клика по элементу
    def click_element(self, locator):
        element = self.find(locator)
        element.click()

    def wait_for_page_load(self, url):
        """
        Ждет загрузки страницы с указанным URL.
        :param url: URL страницы, которую нужно дождаться.
        """
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.url_to_be(url))

    # Общий метод для получения атрибута элемента
    def get_attribute_of_element(self, locator, attribute):
        element = self.find(locator)
        return element.get_attribute(attribute)

    # Общий метод для получения текста элемента
    def get_text_of_element(self, locator):
        element = self.find(locator)
        return element.text

    # Общий метод для получения текста разделов из шапки
    @staticmethod
    def get_text_of_elements(element):
        return element.text

    # Общий метод. Наводит курсор на выпадающий список
    def move_cursor_to_element(self, locator):
        element = self.browser.find_element(*locator)
        self.actions.move_to_element(element).perform()

    # Общий метод. Снимает фокус с выпадающего списка
    def defocus_element(self):
        # Перемещает курсор на 10 пикселей вправо и 10 пикселей вниз от текущего положения
        self.actions.move_by_offset(500, 10).perform()

    # Общий метод. Закрывает модальное окно через оверлей
    def close_modal_via_overlay(self, overlay_locator):
        overlay = self.find_element(*overlay_locator)
        self.actions.move_to_element_with_offset(overlay, 300, 10).click().perform()

    # Общий метод. Проходимся циклом по разделу в шапке сайта.
    def get_elements_text_header(self, locator):
        try:
            elements = self.browser.find_elements(*locator)
            elements_text = [self.remove_newlines(element) for element in elements]
            print(elements_text)
            return elements_text
        except NoSuchElementException:
            # Возвращаем пустой список, если элементы не найдены
            return []

    # Общий метод. Проходимся циклом по каждому элементу в форме обратной связи и возвращаем текст.
    def get_elements_text_form(self, locator):
        try:
            elements = self.browser.find_elements(*locator)
            elements_text = [element.text for element in elements]
            print(elements_text)
            return elements_text
        except NoSuchElementException:
            # Возвращаем пустой список, если элементы не найдены
            return []

    # Общий метод для получения и прокрутки страницы до элемента
    def get_element_scroll_to_element(self, locator):
        element = self.find_element(*locator)
        actions = ActionChains(self.browser)
        actions.move_to_element(element).perform()
        return element

    def wait_for_element(self, locator):
        try:
            WebDriverWait(self.browser, 15).until(element_to_be(locator))
        except TimeoutException:
            return False
        return True

    # Открываем главную страницу
    def open(self, url=None):
        if url is not None:
            self.browser.get(url)
        else:
            self.browser.get(URL)

    # Открываем страницу каталога
    def open_catalog(self):
        self.browser.get(f'{URL}{CHAPTER_CATALOG}')

    # Возвращаем текущую страницу
    def get_current_url(self):
        return self.browser.current_url

    # Нажимает на оверлей для закрытия окна "Выберите Ваш регион"
    def slider_click(self):
        self.find_element(*slider).click()

    # Метод удаляет переносы строк. Используется для тестов в шапки сайта

    def remove_newline(self, locator):
        """
        Находит элемент по указанному локатору и возвращает его текст без переносов строк.

        :param locator: кортеж, содержащий стратегию поиска и значение локатора
        :return: str
        """
        element = self.find_element(*locator)
        text = element.text
        return text.replace('\n', ' ')

    # Метод удаляет переносы строк. Используется для тестов в форме обратной связи
    def remove_newlines(self, element):
        """
        Принимает WebElement и возвращает его текст без переносов строк.

        :param element: WebElement
        :return: str
        """
        text = element.text
        return text.replace('\n', ' ')

        # Метод для генерации букв, цифр, спец. символов

    @staticmethod
    def generate_random_string(length, char_type):
        """
        Генерирует строку заданной длины из указанного набора символов.

        Args:
            length (int): Длина строки.
            char_type (str): Тип символов, из которых будет генерироваться строка.
                Возможные значения: 'russian_letters', 'letters', 'digits', 'punctuation'.

        Returns:
            str: Сгенерированная строка.
        """
        if char_type == 'russian_letters':
            chars = RUSSIAN_LETTERS
        elif char_type == 'letters':
            chars = string.ascii_letters
        elif char_type == 'digits':
            chars = string.digits
        elif char_type == 'punctuation':
            chars = PUNCTUATION
        else:
            raise ValueError(
                "Неверный тип символов. Допустимые значения: 'russian_letters', 'letters', 'digits', 'punctuation'.")

        return ''.join(random.choice(chars) for _ in range(length))

    # Метод генерирует имя или цифры
    #@staticmethod
    #def generate_random_string(length, string_type='russian_letters'):
    # Русский алфавит в верхнем и нижнем регистре
    #russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    #digits = string.digits  # Использование встроенного модуля string для получения цифр

    #if string_type == 'russian_letters':
    #characters = russian_alphabet
    #elif string_type == 'digits':
    #characters = digits
    #else:
    #raise ValueError('Invalid string_type. Use "russian_letters" or "digits".')

    # Генерируем строку случайных символов заданной длины
    #return ''.join(random.choice(characters) for _ in range(length))

    # Нажимает "Добавить в корзину" у карточки товара
    def button_click_cards(self):
        self.click_element(button_card)

    # Нажимает на иконку корзины в шапке
    def sale_basket_click(self):
        self.click_element(sale_basket)

    # Ожидание после добавления товара в корзину
    def count_one(self):
        return WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element(basket_count, "1")
        )

    def count_two(self):
        return WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element(basket_count, "2")
        )

    def open_basket(self):
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            self.open_catalog()
            self.get_element_scroll_to_element(button_card)
            self.button_click_cards()
            self.count_one()
            self.sale_basket_click()
