import allure

from pages.anrex_main_page import MainPage
from tests.data import CALLBACK_POPUP_TITLE


class TestPopupTitle:

    @allure.title('В модальном окне "Заказать обратный звонок" отображается текст о том, что с пользователем свяжутся"')
    def test_callback_popup_title(self, browser):
        title_back = MainPage(browser)
        title_back.open()
        title_back.click_callback_link()
        assert title_back.get_callback_popup_title() == CALLBACK_POPUP_TITLE
