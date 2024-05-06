from selenium.webdriver.common.by import By

logo = (By.XPATH, '//img[@class="logo d-block"]')
city = (By.CLASS_NAME, 'city_wrap')
popup_city = (By.XPATH, "//h3[text()='Выберите Ваш регион']")
close = (By.XPATH, "//button[@class='callback-close popup-close']")
search = (By.XPATH, "//a[@class='action']")
slider = (By.XPATH, "//div[@class='row header_top']")
first_city = (By.XPATH, "//ul[@class='city_list']/li[1]")
callback_link = (By.XPATH,"//a[@сlass='callback-link']")
