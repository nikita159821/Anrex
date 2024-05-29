import allure

from locators.main_page_locators import review_cards, reviews, review_button
from pages.anrex_main_page import MainPage
from tests.data import REVIEWS_NAME, REVIEWS_DATE, REVIEWS_CONTENT, REVIEWS_BUTTON, READ_REVIEW
from tests.urls import URL, CHAPTER_REVIEWS


class TestHomepageReviews:

    @allure.title('На главной странице отображается блок "Отзывы наших покупателей"')
    def test_homepage_reviews_section_is_displayed(self, browser):
        reviews_section = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            reviews_section.open()
        with allure.step('Скроллим до блока "Отзывы наших покупателей"'):
            reviews_section.get_section_reviews()
        with allure.step('Проверяем, что отображается блок "Отзывы наших покупателей"'):
            assert reviews_section.get_section_reviews().is_displayed()

    @allure.title('Блок "Отзывы наших покупателей" содержит 4 карточки с отзывами')
    def test_four_reviews_displayed(self, browser):
        reviews_displayed = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            reviews_displayed.open()
        with allure.step('Скроллим до блока "Отзывы наших покупателей"'):
            reviews_displayed.get_section_reviews()
        with allure.step('Проверяем, что в блоке "Отзывы наших покупателей" 4 карточки с отзывами'):
            assert len(reviews_displayed.get_sections_reviews()) == 4

    @allure.title('Карточка отзывов содержит имя')
    def test_reviews_name(self, browser):
        reviews_displayed = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            reviews_displayed.open()
        with allure.step('Скроллим до блока "Отзывы наших покупателей"'):
            reviews_displayed.get_section_reviews()
        with allure.step('Проверяем, что в блоке "Отзывы наших покупателей" отображается имя покупателя'):
            assert reviews_displayed.get_review_data()['name'] == REVIEWS_NAME

    @allure.title('Карточка отзывов содержит дату')
    def test_reviews_date(self, browser):
        reviews_displayed = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            reviews_displayed.open()
        with allure.step('Скроллим до блока "Отзывы наших покупателей"'):
            reviews_displayed.get_section_reviews()
        with allure.step('Проверяем, что в блоке "Отзывы наших покупателей" отображается дата отзыва покупателя'):
            assert reviews_displayed.get_review_data()['date'] == REVIEWS_DATE

    @allure.title('# Карточка отзывов содержит текст отзыва')
    def test_reviews_content(self, browser):
        reviews_displayed = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            reviews_displayed.open()
        with allure.step('Скроллим до блока "Отзывы наших покупателей"'):
            reviews_displayed.get_section_reviews()
        with allure.step('Проверяем, что в блоке "Отзывы наших покупателей" отображается текст отзыва покупателя'):
            assert reviews_displayed.get_review_data()['content'] == REVIEWS_CONTENT

    @allure.title('Карточка отзывов содержит рейтинг')
    def test_reviews_stars(self, browser):
        reviews_displayed = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            reviews_displayed.open()
        with allure.step('Скроллим до блока "Отзывы наших покупателей"'):
            reviews_displayed.get_section_reviews()
        with allure.step('Проверяем, что в блоке "Отзывы наших покупателей" отображается рейтинг отзыва покупателя'):
            assert reviews_displayed.get_review_stars().is_displayed()

    @allure.title('При наведении на карточку с отзывом, появляется текст ссылка "Читать отзыв полностью"')
    def test_read_more_link_appears_on_review_card_hover(self, browser):
        review_card_hover = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            review_card_hover.open()
        with allure.step('Скроллим до блока "Отзывы наших покупателей"'):
            review_card_hover.get_section_reviews()
        with allure.step('Добавляем ожидание после скролла'):
            review_card_hover.wait_for_element(review_cards)
        with allure.step('Наводим курсор на карточку с отзывом'):
            review_card_hover.move_cursor_to_element(review_cards)
        with allure.step('Проверяем, что на карточке появляется текст "Читать отзыв полностью"'):
            assert review_card_hover.get_read_more_link_text() == READ_REVIEW

    @allure.title('При нажатии на "Читать отзыв полностью" появляется модальное окно')
    def test_modal_window_opens_when_read_more_link_clicked(self, browser):
        modal_window_opens = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            modal_window_opens.open()
        with allure.step('Скроллим до блока "Отзывы наших покупателей"'):
            modal_window_opens.get_section_reviews()
        with allure.step('Добавляем ожидание после скролла'):
            modal_window_opens.wait_for_element(review_cards)
        with allure.step('Наводим курсор на карточку с отзывом'):
            modal_window_opens.move_cursor_to_element(review_cards)
        with allure.step('Нажимаем кнопку "Читать отзыв полностью"'):
            modal_window_opens.get_read_more_link_click()
        with allure.step('Добавляем ожидание после скролла'):
            modal_window_opens.wait_for_element(review_cards)
        with allure.step('Проверяем, что появилось модальное окно с отзывом'):
            assert modal_window_opens.get_review_popup().is_displayed()

    @allure.title('Модальное окно с отзывом закрывается через крестик')
    def test_review_modal_closes_with_close_button(self, browser):
        modal_close_button = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            modal_close_button.open()
        with allure.step('Скроллим до блока "Отзывы наших покупателей"'):
            modal_close_button.get_section_reviews()
        with allure.step('Добавляем ожидание после скролла'):
            modal_close_button.wait_for_element(review_cards)
        with allure.step('Наводим курсор на карточку с отзывом'):
            modal_close_button.move_cursor_to_element(review_cards)
        with allure.step('Нажимаем кнопку "Читать отзыв полностью"'):
            modal_close_button.get_read_more_link_click()
        with allure.step('Нажимаем на крестик в модальном окне'):
            modal_close_button.click_popup_close_review()
        with allure.step('Проверяем, что модальное окно закрылось и не отображается'):
            assert not modal_close_button.get_review_popup().is_displayed()

    @allure.title('Модальное окно с отзывом закрывается через оверлей')
    def test_review_popup_closes_via_overlay(self, browser):
        closes_via_overlay = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            closes_via_overlay.open()
        with allure.step('Скроллим до блока "Отзывы наших покупателей"'):
            closes_via_overlay.get_section_reviews()
        with allure.step('Добавляем ожидание после скролла'):
            closes_via_overlay.wait_for_element(review_cards)
        with allure.step('Наводим курсор на карточку с отзывом'):
            closes_via_overlay.move_cursor_to_element(review_cards)
        with allure.step('Нажимаем кнопку "Читать отзыв полностью"'):
            closes_via_overlay.get_read_more_link_click()
        with allure.step('Закрываем модальное окно через оверлей'):
            closes_via_overlay.close_modal_via_overlay(reviews)
        with allure.step('Проверяем, что модальное окно закрылось и не отображается'):
            assert not closes_via_overlay.get_review_popup().is_displayed()

    @allure.title('В блоке "Отзывы наших покупателей" отображается кнопка "Смотреть все отзывы"')
    def test_visibility_of_view_all_reviews_button(self, browser):
        reviews_button = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            reviews_button.open()
        with allure.step('Скроллим до блока "Отзывы наших покупателей"'):
            reviews_button.get_section_reviews()
        with allure.step('Проверяем, что отображается кнопка "Смотреть все отзывы"'):
            assert reviews_button.get_text_button_review() == REVIEWS_BUTTON

    @allure.title('По клику на "Смотреть все отзывы" редирект на страницу с отзывами.')
    def test_redirect_to_reviews_page_on_view_all_reviews_click(self, browser):
        redirect_to_reviews = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            redirect_to_reviews.open()
        with allure.step('Скроллим до блока "Отзывы наших покупателей"'):
            redirect_to_reviews.get_section_reviews()
        with allure.step('Добавляем ожидание после скролла'):
            redirect_to_reviews.wait_for_element(review_button)
        with allure.step('Нажимаем кнопку "Смотреть все отзывы"'):
            redirect_to_reviews.button_review_click()
        with allure.step('Проверяем, что открылась страница со всеми отзывами'):
            assert redirect_to_reviews.get_current_url() == f'{URL}{CHAPTER_REVIEWS}'
