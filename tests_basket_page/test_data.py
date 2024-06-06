import random
import string
from tests_basket_page.data import BASKET_NAME, BASKET_RANDOM_NAME, BASKET_CITY_INPUT, BASKET_RANDOM_CITY, \
    BASKET_STREET_INPUT, BASKET_RANDOM_STREET, BASKET_RANDOM_HOUSE, BASKET_BODY_INPUT, BASKET_RANDOM_BODY, \
    BASKET_RANDOM_FLAT, BASKET_FLAT_INPUT
from tests_main_page.data import RUSSIAN_LETTERS, PUNCTUATION


class TestData:
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

    @staticmethod
    def generate_test_name():
        for name in BASKET_NAME + BASKET_RANDOM_NAME:
            city = TestData.generate_random_string(random.randint(5, 20), 'russian_letters')
            street = TestData.generate_random_string(random.randint(3, 5), 'russian_letters')
            house = TestData.generate_random_string(random.randint(2, 2), 'digits')
            body = TestData.generate_random_string(random.randint(2, 3), 'digits')
            flat = TestData.generate_random_string(random.randint(2, 3), 'digits')
            phone = TestData.generate_random_string(50, 'digits')
            mail = TestData.generate_random_string(random.randint(5, 20), 'letters') + '@example.com'
            comment = TestData.generate_random_string(random.randint(10, 50), 'russian_letters')
            yield name, city, street, house, body, flat, phone, mail, comment

    @staticmethod
    def generate_test_city():
        for city in BASKET_CITY_INPUT + BASKET_RANDOM_CITY:
            name = TestData.generate_random_string(random.randint(10, 20), 'russian_letters')
            street = TestData.generate_random_string(random.randint(3, 5), 'russian_letters')
            house = TestData.generate_random_string(random.randint(2, 2), 'digits')
            body = TestData.generate_random_string(random.randint(2, 3), 'digits')
            flat = TestData.generate_random_string(random.randint(2, 3), 'digits')
            phone = TestData.generate_random_string(50, 'digits')
            mail = TestData.generate_random_string(random.randint(5, 20), 'letters') + '@example.com'
            comment = TestData.generate_random_string(random.randint(10, 50), 'russian_letters')
            yield name, city, street, house, body, flat, phone, mail, comment

    @staticmethod
    def generate_test_street():
        for street in BASKET_STREET_INPUT + BASKET_RANDOM_STREET:
            city = TestData.generate_random_string(random.randint(5, 20), 'russian_letters')
            name = TestData.generate_random_string(random.randint(10, 20), 'russian_letters')
            house = TestData.generate_random_string(random.randint(2, 2), 'digits')
            body = TestData.generate_random_string(random.randint(2, 3), 'digits')
            flat = TestData.generate_random_string(random.randint(2, 3), 'digits')
            phone = TestData.generate_random_string(50, 'digits')
            mail = TestData.generate_random_string(random.randint(5, 20), 'letters') + '@example.com'
            comment = TestData.generate_random_string(random.randint(10, 50), 'russian_letters')
            yield name, city, street, house, body, flat, phone, mail, comment

    @staticmethod
    def generate_test_house():
        for house in BASKET_RANDOM_HOUSE:
            name = TestData.generate_random_string(random.randint(10, 20), 'russian_letters')
            city = TestData.generate_random_string(random.randint(5, 20), 'russian_letters')
            street = TestData.generate_random_string(random.randint(3, 5), 'russian_letters')
            body = TestData.generate_random_string(random.randint(2, 3), 'digits')
            flat = TestData.generate_random_string(random.randint(2, 3), 'digits')
            phone = TestData.generate_random_string(50, 'digits')
            mail = TestData.generate_random_string(random.randint(5, 20), 'letters') + '@example.com'
            comment = TestData.generate_random_string(random.randint(10, 50), 'russian_letters')
            yield name, city, street, house, body, flat, phone, mail, comment

    @staticmethod
    def generate_test_body():
        for body in BASKET_BODY_INPUT + BASKET_RANDOM_BODY:
            city = TestData.generate_random_string(random.randint(5, 20), 'russian_letters')
            name = TestData.generate_random_string(random.randint(10, 20), 'russian_letters')
            house = TestData.generate_random_string(random.randint(2, 2), 'digits')
            street = TestData.generate_random_string(random.randint(3, 5), 'russian_letters')
            flat = TestData.generate_random_string(random.randint(2, 3), 'digits')
            phone = TestData.generate_random_string(50, 'digits')
            mail = TestData.generate_random_string(random.randint(5, 20), 'letters') + '@example.com'
            comment = TestData.generate_random_string(random.randint(10, 50), 'russian_letters')
            yield name, city, street, house, body, flat, phone, mail, comment

    @staticmethod
    def generate_test_flat():
        for flat in BASKET_FLAT_INPUT + BASKET_RANDOM_FLAT:
            city = TestData.generate_random_string(random.randint(5, 20), 'russian_letters')
            name = TestData.generate_random_string(random.randint(10, 20), 'russian_letters')
            house = TestData.generate_random_string(random.randint(2, 2), 'digits')
            street = TestData.generate_random_string(random.randint(3, 5), 'russian_letters')
            body = TestData.generate_random_string(random.randint(2, 3), 'digits')
            phone = TestData.generate_random_string(50, 'digits')
            mail = TestData.generate_random_string(random.randint(5, 20), 'letters') + '@example.com'
            comment = TestData.generate_random_string(random.randint(10, 50), 'russian_letters')
            yield name, city, street, house, body, flat, phone, mail, comment

