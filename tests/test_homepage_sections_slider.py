import allure

from locators.main_page_locators import img, button_up, button_down
from pages.anrex_main_page import MainPage
from tests.data import TEXT_SLIDER_LIVING_ROOMS, TEXT_SLIDER_CABINETS, TITLE_SLIDER
from tests.urls import URL, IMG


class TestSectionSlider:

    @allure.title('На главной странице отображается слайдер разделов')
    def test_homepage_sections_slider(self, browser):
        sections_slider = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            sections_slider.open()
        with allure.step('Скроллим до блока со слайдером разделов'):
            sections_slider.get_slider()
        with allure.step('Проверяем, что отображается слайдер разделов'):
            assert sections_slider.get_slider().is_displayed()

    @allure.title('Переключение разделов в карусели через стрелку вверх')
    def test_switch_carousel_section_up(self, browser):
        carousel_section = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            carousel_section.open()
        with allure.step('Скроллим до блока со слайдером разделов'):
            carousel_section.get_slider()
        with allure.step('Добавляем ожидание после скролла'):
            carousel_section.wait_for_element(button_up)
        with allure.step('Нажимаем кнопку вверх на слайдере разделов'):
            carousel_section.click_up_slider()
        with allure.step('Проверяем, что произошло переключение на раздел "Гостиных"'):
            assert carousel_section.get_text_slider_living_rooms() == TEXT_SLIDER_LIVING_ROOMS

    @allure.title('Переключение разделов в карусели через стрелку вверх')
    def test_switch_carousel_section_down(self, browser):
        carousel_section = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            carousel_section.open()
        with allure.step('Скроллим до блока со слайдером разделов'):
            carousel_section.get_slider()
        with allure.step('Добавляем ожидание после скролла'):
            carousel_section.wait_for_element(button_down)
        with allure.step('Нажимаем кнопку вниз на слайдере разделов'):
            carousel_section.click_down_slider()
        with allure.step('Проверяем, что произошло переключение на раздел "Кабинетов"'):
            assert carousel_section.get_text_slider_cabinets() == TEXT_SLIDER_CABINETS

    @allure.title('В каруселе разделов на главной странице отображается текст "Мебель для"')
    def test_carousel_section_text_furniture_is_displayed(self, browser):
        furniture_is_displayed = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            furniture_is_displayed.open()
        with allure.step('Скроллим до блока со слайдером разделов'):
            furniture_is_displayed.get_slider()
        with allure.step('Проверяем, что в слайдере с разделами отображается текст "Мебель для"'):
            assert furniture_is_displayed.get_text_slider_title() == TITLE_SLIDER

    @allure.title('При переключении разделов через карусель, меняется фото раздела')
    def test_section_photo_changes_carousel(self, browser):
        photo_changes = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            photo_changes.open()
        with allure.step('Скроллим до блока со слайдером разделов'):
            photo_changes.get_slider()
        with allure.step('Добавляем ожидание после скролла'):
            photo_changes.wait_for_element(button_up)
        with allure.step('Нажимаем кнопку вверх на слайдере разделов'):
            photo_changes.click_up_slider()
        with allure.step('Ждем смены раздела и фото'):
            photo_changes.wait_for_element(img)
        with allure.step('Проверяем, что полученное изображение совпадает с ожидаемым'):
            assert photo_changes.get_slider_img() == f'{URL}{IMG}'

