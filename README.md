# Тесты для проекта Anrex

## Описание
Тесты проверяют функциональность главной страницы и корзины. Настроена интеграция с TMS системой - doqa. Тесты запускаются автоматически один раз в день, а результаты отправляются в doqa.

## Установка зависимостей
Все необходимые пакеты для выполнения тестов перечислены в файле requirements.txt. Вы можете установить их с помощью следующей команды:

pip install -r requirements.txt

## Запуск тестов
Тесты можно запустить с помощью команды:

pytest tests_basket_page/tests_main_page --alluredir=allure-results --junitxml=junit-report.xml
pytest tests_main_page/path/to/your_script.py
pytest tests_basket_page/path/to/your_script.py

## Интеграция с doqa
Результаты тестов автоматически отправляются в doqa. Для этого используется следующий код:

- name: Send junit report
  run: |
    ./doqa-cli report https://rumerkulov.doqa.app/api/autotests/report ${{ secrets.TOKEN_DOQA }} modified_report.xml

Здесь используется секрет GitHub TOKEN_DOQA для авторизации в doqa.