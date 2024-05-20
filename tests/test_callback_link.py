import allure

from locators.main_page_locators import callback_link
from pages.anrex_main_page import MainPage


class TestCallbackLink:

    @allure.title('В шапке отображается текст-ссылка "Заказать обратный звонок"')
    def test_callback_link(self, browser):
        link = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            link.open()
        with allure.step('Добавляем ожидание'):
            link.wait(callback_link)
        with allure.step('Находим элемент на странице и проверяем, что отображается'):
            assert link.get_callback_link().is_displayed()
