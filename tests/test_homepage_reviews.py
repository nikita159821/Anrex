from locators.main_page_locators import review_cards, reviews
from pages.anrex_main_page import MainPage
from tests.data import REVIEWS_NAME, REVIEWS_DATE, REVIEWS_CONTENT


class TestHomepageReviews:

    # На главной странице отображается блок "Отзывы наших покупателей"
    def test_homepage_reviews_section_is_displayed(self, browser):
        reviews_section = MainPage(browser)
        reviews_section.open()
        assert reviews_section.get_section_reviews().is_displayed()

    # Блок "Отзывы наших покупателей" содержит 4 карточки с отзывами
    def test_four_reviews_displayed(self, browser):
        reviews_displayed = MainPage(browser)
        reviews_displayed.open()
        reviews_displayed.get_section_reviews()
        assert len(reviews_displayed.get_sections_reviews()) == 4

    # Карточка отзывов содержит имя
    def test_reviews_name(self, browser):
        reviews_displayed = MainPage(browser)
        reviews_displayed.open()
        reviews_displayed.get_section_reviews()
        assert reviews_displayed.get_review_data()['name'] == REVIEWS_NAME

    # Карточка отзывов содержит дату
    def test_reviews_date(self, browser):
        reviews_displayed = MainPage(browser)
        reviews_displayed.open()
        reviews_displayed.get_section_reviews()
        assert reviews_displayed.get_review_data()['date'] == REVIEWS_DATE

    # Карточка отзывов содержит текст отзыва
    def test_reviews_content(self, browser):
        reviews_displayed = MainPage(browser)
        reviews_displayed.open()
        reviews_displayed.get_section_reviews()
        assert reviews_displayed.get_review_data()['content'] == REVIEWS_CONTENT

    # Карточка отзывов содержит рейтинг
    def test_reviews_stars(self, browser):
        reviews_displayed = MainPage(browser)
        reviews_displayed.open()
        reviews_displayed.get_section_reviews()
        assert reviews_displayed.get_review_stars().is_displayed()

    # При наведение на карточку с отзывом, появляется текст ссылка "Читать отзыв полностью"
    def test_read_more_link_appears_on_review_card_hover(self, browser):
        review_card_hover = MainPage(browser)
        review_card_hover.open()
        review_card_hover.get_section_reviews()
        review_card_hover.move_cursor_to_element(review_cards)
        assert review_card_hover.get_read_more_link_text() == "Читать отзыв полностью"

    # При нажатии на "Читать отзыв полностью" появляется модальное окно
    def test_modal_window_opens_when_read_more_link_clicked(self, browser):
        modal_window_opens = MainPage(browser)
        modal_window_opens.open()
        modal_window_opens.get_section_reviews()
        modal_window_opens.move_cursor_to_element(review_cards)
        modal_window_opens.get_read_more_link_click()
        assert modal_window_opens.get_review_popup().is_displayed()

    # Модальное окно с отзывом закрывается через крестик
    def test_review_modal_closes_with_close_button(self, browser):
        modal_close_button = MainPage(browser)
        modal_close_button.open()
        modal_close_button.get_section_reviews()
        modal_close_button.move_cursor_to_element(review_cards)
        modal_close_button.get_read_more_link_click()
        modal_close_button.click_popup_close_review()
        assert not modal_close_button.get_review_popup().is_displayed()

    # Модальное окно с отзывом закрывается через оверлей
    def test_review_popup_closes_via_overlay(self, browser):
        closes_via_overlay = MainPage(browser)
        closes_via_overlay.open()
        closes_via_overlay.get_section_reviews()
        closes_via_overlay.move_cursor_to_element(review_cards)
        closes_via_overlay.get_read_more_link_click()
        closes_via_overlay.close_modal_via_overlay(reviews)
        assert not closes_via_overlay.get_review_popup().is_displayed()
