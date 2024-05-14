from pages.anrex_main_page import MainPage
from tests.data import TEXT_SLIDER_LIVING_ROOMS, TEXT_SLIDER_CABINETS, TITLE_SLIDER


class TestSectionSlider:

    # На главной странице отображается слайдер разделов
    def test_homepage_sections_slider(self, browser):
        sections_slider = MainPage(browser)
        sections_slider.open()
        assert sections_slider.get_slider().is_displayed()

    # Переключение разделов в карусели через стрелку вверх
    def test_switch_carousel_section_up(self, browser):
        carousel_section = MainPage(browser)
        carousel_section.open()
        carousel_section.get_slider()
        carousel_section.click_up_slider()
        assert carousel_section.get_text_slider_living_rooms() == TEXT_SLIDER_LIVING_ROOMS

    # Переключение разделов в карусели через стрелку вверх
    def test_switch_carousel_section_down(self, browser):
        carousel_section = MainPage(browser)
        carousel_section.open()
        carousel_section.get_slider()
        carousel_section.click_down_slider()
        assert carousel_section.get_text_slider_cabinets() == TEXT_SLIDER_CABINETS

    # В каруселе разделов на главной странице отображается текст "Мебель для"
    def test_carousel_section_text_furniture_is_displayed(self, browser):
        furniture_is_displayed = MainPage(browser)
        furniture_is_displayed.open()
        furniture_is_displayed.get_slider()
        assert furniture_is_displayed.get_text_slider_title() == TITLE_SLIDER
