import allure
from locators.main_page_locators import button_card
from pages.basket_page import BasketPage


class TestCartPageImageDisplay:
    @allure.title('В корзине отображается фото товара добавленного из каталога')
    def test_display_product_name_basket(self, browser):
        display_product_name = BasketPage(browser)
        with allure.step('Открываем страницу каталога'):
            display_product_name.open_catalog()
        with allure.step('Скролл до карточки товара'):
            display_product_name.get_element_scroll_to_element(button_card)
        with allure.step('Сохраняем название на товар из каталога'):
            catalog_name = display_product_name.get_text_name_products_catalog()
        with allure.step('Добавляем товар в корзину '):
            display_product_name.button_click_cards()
        with allure.step('Ожидание пока добавится товар в корзину'):
            display_product_name.count_one()
        with allure.step('Открываем корзину'):
            display_product_name.sale_basket_click()
        with allure.step('Проверяем, что в корзине отображается название товара добавленного из каталога'):
            assert display_product_name.get_text_name_products_basket() == catalog_name
