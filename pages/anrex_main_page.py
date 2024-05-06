from locators.main_page_locators import logo, city, popup_city, close, search, slider, first_city
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    # Получаем, сохраняем и возвращаем ссылку на img
    def get_logo_src(self):
        logo_element = self.find_element(*logo)
        logo_src = logo_element.get_attribute('src')
        return logo_src

    # Нажимаем на лого
    def logo_click(self):
        self.find_element(*logo).click()

    def city_wrap(self):
        city_wrap = self.find_element(*city)
        return city_wrap

    def city_wrap_click(self):
        self.find_element(*city).click()

    def popup_city(self):
        popup = self.find_element(*popup_city)
        return popup

    def close_popup_click(self):
        self.find_element(*close).click()

    def search(self):
        search_ = self.find_element(*search).click()
        return search_

    def slider_click(self):
        self.find_element(*slider).click()

    def first_sity(self):
        popup = self.find_element(*first_city)
        first_city_text = popup.text
        return first_city_text
