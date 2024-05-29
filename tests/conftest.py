from selenium import webdriver
import pytest
import sys
import os
from selenium.webdriver.chrome.options import Options

# Добавляем путь к директории "pages"
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--headless=new")
    driver_browser = webdriver.Chrome(options=options)
    driver_browser.maximize_window()
    yield driver_browser
    driver_browser.quit()