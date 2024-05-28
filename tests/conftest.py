from selenium import webdriver
import pytest
import sys
import os
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
# Добавляем путь к директории "pages"
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    browser_name = request.param
    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless=new")
        firefox_options.set_preference("marionette.logLevel", "DEBUG")

        # Явно указываем путь к Geckodriver
        gecko_driver_path = "/home/nikita/WebDriver/bin/geckodriver"
        firefox_service = FirefoxService(executable_path=gecko_driver_path)
        driver = webdriver.Firefox(options=firefox_options, service=firefox_service)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()
    yield driver
    driver.quit()

