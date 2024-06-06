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

BASKET_CITY = 'М'
STREET = 'Ул'
HOUSE = '10'
BODY = '12345'
FLAT = '101'
PHONE_NUMBER = '+7 123 456 7890'
EMAIL = 'example@example.com'
COMMENT = 'Тестовый комментарий'


BASKET_FLAT_INPUT = [
    '25'
]

BASKET_PHONE_INPUT = [
    9999999999
]

BASKET_MAIL_INPUT = [
    'test@yandex.ru'
]

BASKET_COMMENT_INPUT = [
    'Тестовый комментарий'
]