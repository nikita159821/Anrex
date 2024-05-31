import allure

from pages.anrex_main_page import MainPage
from tests_main_page.data import CALLBACK_POPUP_TITLE


class TestPopupTitle:

    @allure.title('В модальном окне "Заказать обратный звонок" отображается текст о том, что с пользователем свяжутся"')
    def test_callback_popup_title(self, browser):
        title_back = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            title_back.open()
        with allure.step('Нажимаем на "Заказать обратный звонок"'):
            title_back.click_callback_link()
        with allure.step('Получаем текст в форме "Заказать обратный звонок" и сравниваем с ожидаемым'):
            assert title_back.get_callback_popup_title() == CALLBACK_POPUP_TITLE
