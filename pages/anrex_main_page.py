from locators.main_page_locators import logo, city, popup_city, close, search, first_city, callback_link
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

    # Возвращает выбарнный город на странице
    def city_wrap(self):
        city_wrap = self.find_element(*city)
        return city_wrap

    # Нажимает на город на сайте
    def city_wrap_click(self):
        self.find_element(*city).click()

    # Возвращает тайтл "Выберите Ваш регион"
    def popup_city(self):
        popup = self.find_element(*popup_city)
        return popup

    # Нажимает на крести в модальном окне выбора города
    def close_popup_click(self):
        self.find_element(*close).click()

    # Возвращает иконку поиска на главной странице  "Выберите Ваш регион"
    def search(self):
        search_ = self.find_element(*search).click()
        return search_

    # Находит первый город в модалке "Выберите Ваш регион"
    def first_sity(self):
        popup = self.find_element(*first_city)
        first_city_text = popup.text
        return first_city_text

    # Возвращает текст-ссылку "Заказать обратный звонок"
    def get_callback_link(self):
        link = self.find_element(*callback_link)
        return link
