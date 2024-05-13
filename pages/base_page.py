import random
import string

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import slider
from tests.data import RUSSIAN_LETTERS
from tests.urls import URL, CATALOG


# Класс для кастомного условия ожидания
class element_text_to_be:
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

    def wait_for_element_text_to_be(self, locator):
        try:
            WebDriverWait(self.browser, 10).until(element_text_to_be(locator))
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
        self.browser.get(f'{URL}{CATALOG}')

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

