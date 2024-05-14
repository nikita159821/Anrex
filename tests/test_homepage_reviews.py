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
        reviews_section = reviews_displayed.get_sections_reviews()
        assert len(reviews_section) == 4

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