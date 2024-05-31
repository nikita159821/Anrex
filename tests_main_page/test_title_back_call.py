import allure

from pages.anrex_main_page import MainPage
from tests_main_page.data import TITLE_BACK_CALL


class TestTitle:

    @allure.title('В "Заявка на обратный звонок" отображается тайтл "Заявка на обратный звонок"')
    def test_title_back_call(self, browser):
        title_back = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            title_back.open()
        with allure.step('Нажимаем "Заказать обратный звонок"'):
            title_back.click_callback_link()
        with allure.step('Проверяем, что в модальном оке есть тайтл "Заявка на обратный звонок"'):
            assert title_back.get_back_call() == TITLE_BACK_CALL
