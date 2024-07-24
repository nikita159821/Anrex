import allure

from locators.basket_page_locators import image_card, image_card_basket
from locators.main_page_locators import button_card
from pages.basket_page import BasketPage


class TestCartPageImageDisplay:
    @allure.title('В корзине отображается фото товара добавленного из каталога')
    def test_display_product_image_in_cart(self, browser):
        display_product_image = BasketPage(browser)
        with allure.step('Открываем страницу каталога'):
            display_product_image.open_catalog()
        with allure.step('Скролл до карточки товара'):
            display_product_image.get_element_scroll_to_element(button_card)
        with allure.step('Сохраняем ссылку на фото товара из каталога'):
            catalog_image_url = display_product_image.get_attribute_of_element(image_card, 'src')
        with allure.step('Добавляем товар в корзину '):
            display_product_image.button_click_cards()
        with allure.step('Ожидание пока добавится товар в корзину'):
            display_product_image.count_one()
        with allure.step('Открываем корзину'):
            display_product_image.sale_basket_click()
        with allure.step('Сохраняем ссылку на фото товара в корзине'):
            cart_image_url = display_product_image.get_attribute_of_element(image_card_basket, 'src')
        with allure.step('Удаляем лишние символы  у фото из корзины'):
            cart_image_name = cart_image_url.replace("resize_cache/", "")
        with allure.step('Удаляем лишние символы  у фото из корзины'):
            cart_image_name = cart_image_name.replace("160_160_1/", "")
        with allure.step('Сравниваем ссылку на фото товара из каталога и корзины'):
            assert catalog_image_url == cart_image_name
