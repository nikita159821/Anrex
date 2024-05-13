from pages.anrex_main_page import MainPage


class TestDiscountedProducts:

    # На главной странице отображается блок "Товары со скидками"
    def test_discounted_products(self, browser):
        discounted = MainPage(browser)
        discounted.open()
        discounted_products = discounted.discounted_products()
        assert discounted_products.is_displayed()

