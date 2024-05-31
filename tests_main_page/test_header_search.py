import allure

from locators.main_page_locators import search_line, search_line_close
from pages.anrex_main_page import MainPage
from tests_main_page.data import SEARCH


class TestDisplaysSearch:

    @allure.title('Проверка, что отображается иконка поиска в шапке сайта')
    def test_header_displays_search(self, browser):
        displays_search = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            displays_search.open()
        with allure.step('Находим иконку поиска в шапке сайта и сравниваем с ожидаемой'):
            assert displays_search.get_search_cvg() == SEARCH

    @allure.title('Проверка отображение строки поиска в шапке сайта.')
    def test_search_click(self, browser):
        search_click = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            search_click.open()
        with allure.step('Нажимаем на иконку поиска'):
            search_click.get_search_click()
        with allure.step('Ожидаем появление строки'):
            search_click.wait_for_element(search_line)
        with allure.step('Проверяем, что появилась строка поиска'):
            assert search_click.get_search_input().is_displayed()

    @allure.title('По нажатию строка поиска закрывается')
    def test_search_click_close(self, browser):
        search_click_close = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            search_click_close.open()
        with allure.step('Нажимаем на иконку поиска'):
            search_click_close.get_search_click()
        with allure.step('Нажимаем на иконку поиска еще раз'):
            search_click_close.get_search_active()
            with allure.step('Ожидаем закрытие строки'):
                search_click_close.wait_for_element(search_line_close)
        with allure.step('Проверяем, что строка поиска больше не отображается'):
            assert search_click_close.get_search_input_close() is not None
