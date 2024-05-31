import os
import sys
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(params=['chrome'])
def browser(request):
    browser_name = request.param
    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()
        #firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options=firefox_options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()
    yield driver
    driver.quit()
