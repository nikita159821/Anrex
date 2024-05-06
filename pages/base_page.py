from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import slider
from tests.urls import URL


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find_element(self, *args):
        return self.browser.find_element(*args)

    def wait(self, locator):
        WebDriverWait(self.browser, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.browser.find_element(*locator)

    # Открываем страницу
    def open(self):
        self.browser.get(URL)

    # Возвращаем текущую страницу
    def get_current_url(self):
        return self.browser.current_url

    # Нажимает на оверлей для закрытия окна "Выберите Ваш регион"
    def slider_click(self):
        self.find_element(*slider).click()
