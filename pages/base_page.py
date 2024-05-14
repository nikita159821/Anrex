import random
import string

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import slider
from tests.data import RUSSIAN_LETTERS
from tests.urls import URL, CHAPTER_CATALOG


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

    # Общий метод. Наводит курсорс на выпадающий список
    def move_cursor_to_element(self, locator):
        element = self.browser.find_element(*locator)
        self.actions.move_to_element(element).perform()

    # Общий метод. снимает фокус с выпадающего списка
    def defocus_element(self):
        # Перемещает курсор на 10 пикселей вправо и 10 пикселей вниз от текущего положения
        self.actions.move_by_offset(500, 10).perform()

    # Общий метод. Закрывает модальное окно через оверлей
    def close_modal_via_overlay(self, overlay_locator):
        overlay = self.find_element(*overlay_locator)
        self.actions.move_to_element_with_offset(overlay, 10, 10).click().perform()

    # Общий метод. Проходимся циклом по разделу в шапке сайта.
    def get_elements_text(self, locator):
        try:
            elements = self.browser.find_elements(*locator)
            elements_text = [self.remove_newline(element) for element in elements]
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
            WebDriverWait(self.browser, 10).until(element_to_be(locator))
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

    # Метод удаляет переносы строк
    @staticmethod
    def remove_newline(element):
        """
        Удаляет переносы строк из текста элемента.

        :param element: WebElement
        :return: str
        """
        text = element.text
        actual_text = text.replace('\n', ' ')
        return actual_text

    # Метод для генерации букв, цифра, спец.символов
    @staticmethod
    def generate_name_and_phone(length, char_type):
        """
        Генерирует строку заданной длины из указанного набора символов.

        Args:
            length (int): Длина строки.
            char_type (str): Тип символов, из которых будет генерироваться строка.
                Возможные значения: 'russian_letters','letters', 'digits', 'punctuation'.

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
            chars = string.punctuation
        else:
            raise ValueError("Неверный тип символов. Допустимые значения: 'russian_letters', 'digits', 'punctuation'.")

        return ''.join(random.choice(chars) for _ in range(length))

    # Метод генерирует имя
    @staticmethod
    def generate_random_russian_string(length):
        # Русский алфавит в верхнем и нижнем регистре
        russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

        # Генерируем строку случайных букв заданной длины
        return ''.join(random.choice(russian_alphabet) for _ in range(length))
