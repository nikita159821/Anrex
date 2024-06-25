#import time
#import allure
#from pages.anrex_main_page import MainPage

# ЭТОТ БЛОК ОТКЛЮЧЕН НА DEV, А ТЕСТЫ ЗАПУСКАЮТСЯ ТОЛЬКО ЗДЕСЬ
#class TestDiscountedProducts:

    #@allure.title('На главной странице отображается блок "Товары со скидками"')
    #def test_discounted_products(self, browser):
        #discounted = MainPage(browser)
        #with allure.step('Открываем главную страницу'):
            #discounted.open()
        #with allure.step('Добавляем ожидание'):
            #time.sleep(5)
        #with allure.step('Находим и проверяем блок "Товары со скидками"'):
            #assert discounted.get_discounted_products().is_displayed()

