import time

from pages.anrex_main_page import MainPage
from tests.urls import URL, CHAPTER_CATALOG, CHAPTER_MATRASI


class TestRedirectBedsSection:
    def test_redirect_krovati_i_matrasi(self, browser):
        redirect_krovati = MainPage(browser)
        redirect_krovati.open()
        redirect_krovati.get_popular_categories()
        redirect_krovati.click_popular_categories()
        assert redirect_krovati.get_current_url() == f'{URL}{CHAPTER_CATALOG}{CHAPTER_MATRASI}'
