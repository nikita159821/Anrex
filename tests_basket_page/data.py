import random

from pages.anrex_main_page import MainPage

INPUT_FULL_NAME = "ФИО*"
INPUT_DELIVERY_CITY = "Город доставки*"
INPUT_STREET = "Улица*"
INPUT_HOUSE = "Дом*"
INPUT_BODY = "Корпус"
INPUT_FLAT = "Квартира"
INPUT_PHONE_NUMBER = "Номер телефона*"
INPUT_MAIL = "E-mail"
INPUT_YOUR_COMMENT = "Ваш комментарий"
INPUT_NAME_PLACEHOLDER = 'Антон Иванов'
INPUT_ADDRESS_PLACEHOLDER = 'Москва'
INPUT_STREET_PLACEHOLDER = 'Проспект Ленина'
INPUT_HOUSE_PLACEHOLDER = '10'
INPUT_BUILDING_PLACEHOLDER = '2Б'
INPUT_APARTMENT_PLACEHOLDER = '200'
INPUT_PHONE_PLACEHOLDER = '+ 7 (999) 000-00-00'
INPUT_EMAIL_PLACEHOLDER = 'ivanova@yandex.ru'
INPUT_COMMENT_PLACEHOLDER = 'Введите Ваш комментарий'
ORDER_CONFIRMATION = 'Подтверждение заказа'
ERROR_INPUTS_BASKET = 'Поле заполнено неверно'
ERROR_INPUT_CITY = 'Минимальная длина поля "Город доставки" не менее 2 символов'
ERROR_INPUT_STREET = 'Минимальная длина поля "Улица" не менее 3 символов'
ERROR_INPUT_HOUSE_digits = 'Максимальное значение поля "Дом" 999'
ERROR_INPUT_HOUSE_russian_letters = 'Поле "Дом" должно быть числовым'
ERROR_INPUT_HOUSE_whitespace = 'Поле "Дом" обязательно для заполнения'
ERROR_INPUT_EMAIl = 'Введен неверный e-mail'
ERROR_INPUT_PHONE_ONE_DIGIT = 'Минимальная длина поля "Номер телефона" не менее 11 символов'

BASKET_RANDOM_NAME = [
    MainPage.generate_random_string(2, 'russian_letters'),
    MainPage.generate_random_string(49, 'russian_letters'),
    MainPage.generate_random_string(50, 'russian_letters'),
    MainPage.generate_random_string(51, 'russian_letters'),
]

BASKET_RANDOM_CITY = [
    MainPage.generate_random_string(2, 'russian_letters'),
    MainPage.generate_random_string(49, 'russian_letters'),
    MainPage.generate_random_string(50, 'russian_letters'),
    MainPage.generate_random_string(51, 'russian_letters'),
]

BASKET_RANDOM_STREET = [
    MainPage.generate_random_string(3, 'russian_letters'),
    MainPage.generate_random_string(50, 'russian_letters'),
    MainPage.generate_random_string(51, 'russian_letters'),
]

BASKET_RANDOM_HOUSE = [
    MainPage.generate_random_string(2, 'digits'),
    MainPage.generate_random_string(3, 'digits'),
]

BASKET_RANDOM_BODY = [
    MainPage.generate_random_string(2, 'digits'),
    MainPage.generate_random_string(5, 'digits')
]

BASKET_RANDOM_FLAT = [
    MainPage.generate_random_string(2, 'digits'),
    MainPage.generate_random_string(5, 'digits')
]

BASKET_RANDOM_COMMENT = [
    MainPage.generate_random_string(4, 'russian_letters'),
    MainPage.generate_random_string(6, 'digits'),
    MainPage.generate_random_string(6, 'punctuation'),
    MainPage.generate_random_string(5, 'letters'),
    MainPage.generate_random_string(3999, 'letters'),
    MainPage.generate_random_string(4000, 'letters')
]

BASKET_STREET_INPUT = [
    'Проспект Ленина',
    '250-летия Челябинска',
    'Арзамасская 3-я'
]

# Пока на паузе. Есть баг связанный с вводом слеша в поле дом
#BASKET_HOUSE_INPUT = [
#'10/10'
#]

BASKET_CITY_INPUT = [
    'Москва',
    'Санкт-петербург'
]

BASKET_NAME = [
    "Иванов Иван Иванович",
    "John Doe",
    "Петрова-Иванова Мария",
    "Мария Иванова"
]

BASKET_RANDOM_NAME_NEGATIVE = [
    '----',
    'Иванов Иван 1',
    'Я Ян'
]

BASKET_BODY_INPUT = [
    '2',
    '2/2'
]

BASKET_FLAT_INPUT = [
    '200',
    '2/3'
]

BASKET_EMAIL_INPUT = [
    'test@yandex.ru',
    'te.st@yandex.ru',
    'te_st@yandex.ru',
    'TEST@YANDEX.RU',
    'test123@yandex.ru',
    'te-st@yandex.ru'
]

BASKET_EMAIL_NEGATIVE = [
    'te...st@yandex.ru',
    'testyandex.ru',
    'test@'
]

BASKET_PHONE_NEGATIVE = [
    '9'
]

BASKET_PHONE_LETTERS = [
    'gfdsgagdsdsfgdf'
]

BASKET_PHONE_TWELVE_DIGIT = [
    '999999999999'
]

BASKET_PHONE_INPUT_MASK = [
    '+7 (9'
]

BASKET_CITY = 'М'
STREET = 'Ул'
HOUSE = '10'
BODY = '12345'
FLAT = '12345'
PHONE_NUMBER = '+7 (999) 999-99-99'
EMAIL = 'te st@yandex.ru'
EXPECTED_EMAIL = 'test@yandex.ru'
COMMENT = 'Тестовый комментарий'

BASKET_PHONE_INPUT = [
    9999999999
]

BASKET_MAIL_INPUT = [
    'test@yandex.ru'
]

BASKET_COMMENT_INPUT = [
    'Тестовый комментарий'
]
NEW_COMMENTS = MainPage.generate_random_string(4001, 'russian_letters'),