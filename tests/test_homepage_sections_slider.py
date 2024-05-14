import time

from pages.anrex_main_page import MainPage
from tests.data import TEXT_SLIDER_LIVING_ROOMS, TEXT_SLIDER_CABINETS


class TestSectionSlider:

    # На главной странице отображается слайдер разделов
    def test_homepage_sections_slider(self, browser):
        sections_slider = MainPage(browser)
        sections_slider.open()
        slider = sections_slider.get_slider()
        assert slider.is_displayed()

    # Переключение разделов в карусели через стрелку вверх
    def test_switch_carousel_section_up(self, browser):
        carousel_section = MainPage(browser)
        carousel_section.open()
        carousel_section.get_slider()
        carousel_section.click_up_slider()
        section = carousel_section.get_text_slider_living_rooms()
        assert section == TEXT_SLIDER_LIVING_ROOMS

    # Переключение разделов в карусели через стрелку вверх
    def test_switch_carousel_section_down(self, browser):
        carousel_section = MainPage(browser)
        carousel_section.open()
        carousel_section.get_slider()
        carousel_section.click_down_slider()
        section = carousel_section.get_text_slider_cabinets()
        assert section == TEXT_SLIDER_CABINETS
