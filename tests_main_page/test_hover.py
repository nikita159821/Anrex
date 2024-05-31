import allure

from pages.anrex_main_page import MainPage
from tests_main_page.data import HOVER


class TestHover:

    @allure.title('В шапке сайта отображается ховер при наведении на "Заказать обратный звонок"')
    def test_hover(self, browser):
        hover = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            hover.open()
        with allure.step('Проверяем, что отображается текст-ховер в шапке сайта'):
            assert hover.get_hover_tooltip_text() == HOVER
