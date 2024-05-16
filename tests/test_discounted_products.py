import allure

from pages.anrex_main_page import MainPage


class TestDiscountedProducts:

    @allure.title('На главной странице отображается блок "Товары со скидками"')
    def test_discounted_products(self, browser):
        discounted = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            discounted.open()
        with allure.step('Находим и проверям блок "Товары со скидками"'):
            assert discounted.get_discounted_products().is_displayed()

