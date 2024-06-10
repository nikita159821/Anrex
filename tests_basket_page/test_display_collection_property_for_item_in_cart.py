import allure

from locators.main_page_locators import button_card
from pages.basket_page import BasketPage


class TestDisplayCollectionProperty:

    @allure.title('В корзине отображается название коллекции товара')
    def test_display_collection_property_for_item_in_cart(self,browser):
        display_collection_property = BasketPage(browser)
        with allure.step('Открываем страницу каталога и добавляем товар в корзину'):
            display_collection_property.open_catalog()
        with allure.step('Скроллим до карточки товара'):
            display_collection_property.get_element_scroll_to_element(button_card)
        with allure.step('Сохраняем название коллекции товара в каталоге'):
            collection_products_catalog = display_collection_property.get_text_collection_products_catalog()
        with allure.step('Добавляем товар в корзину'):
            display_collection_property.button_click_cards()
        with allure.step('Ожидаем пока товар добавится в корзине'):
            display_collection_property.count_one()
        with allure.step('Открываем корзину'):
            display_collection_property.sale_basket_click()
        with allure.step('Проверяем, что в корзине отображается коллекция добавленного товара в корзину'):
            assert display_collection_property.get_text_collection_products_basket() == collection_products_catalog

