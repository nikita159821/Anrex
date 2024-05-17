import allure

from pages.anrex_main_page import MainPage
from tests.urls import URL, CHAPTER_CATALOG, CHAPTER_MATRASI


class TestRedirectBedsSection:

    @allure.title('Редирект в раздел "Кровати и матрасы" из блока "Популярные категории"')
    def test_redirect_krovati_i_matrasi(self, browser):
        redirect_krovati = MainPage(browser)
        with allure.step('Открываем главную страницу'):
            redirect_krovati.open()
        with allure.step('Скроллим до блока "Популярные категории"'):
            redirect_krovati.get_popular_categories()
        with allure.step('Нажимаем на "Кровати и матрасы" в блоке "Популярные категории"'):
            redirect_krovati.click_popular_categories()
        with allure.step('Проверяем, что открылся раздел каталога "Кровати и матрасы"'):
            assert redirect_krovati.get_current_url() == f'{URL}{CHAPTER_CATALOG}{CHAPTER_MATRASI}'
