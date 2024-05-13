from selenium.webdriver.common.by import By

logo = (By.XPATH, '//img[@class="logo d-block"]')
city = (By.CLASS_NAME, 'city_wrap')
popup_city = (By.XPATH, "//h3[text()='Выберите Ваш регион']")
close = (By.XPATH, "//button[@class='callback-close popup-close']")
search = (By.XPATH, "//a[@class='action']")
search_active = (By.XPATH, "//a[@class='action active']")
slider = (By.XPATH, "//div[@class='row header_top']")
first_city = (By.XPATH, "//ul[@class='city_list']/li[1]")
callback_link = (By.XPATH, "//a[@class='callback-link d-sm-none d-md-block']")
hover_text = (By.CSS_SELECTOR, "a.callback-link > span")
title_back_call = (By.XPATH, "//h3[contains(., 'Заявка на обратный')]")
text_back_call = (By.XPATH, "//p[@class='text-center']")
input_name = (By.XPATH, "//input[@id='callback_name']")
input_phone = (By.XPATH, "//input[@id='callback_phone']")
name_placeholder = (By.CSS_SELECTOR, '[placeholder="Антон"]')
phone_placeholder = (By.CSS_SELECTOR, '[placeholder="+7 (960) 345-44-19"]')
name_error = (By.XPATH, "//div[@class='align-items-center d-flex flex-column input-field has-error']")
phone_error = (By.XPATH, "//div[@class='align-items-center d-flex flex-column input-field has-error']")
title_sale = (By.XPATH, "//b[text()='Товары со скидками']")
button_send_application = (By.XPATH, "//input[@id='callback_submit']")
popup_back_call = (By.XPATH, "//p[contains(text(), 'Ваша заявка была направлена')]")
tel_callback = (By.ID, 'tel-callback')
search_cvg = (By.CSS_SELECTOR, ".action > svg:nth-child(1)")
search_line = (By.XPATH, "//input[@id='search-input']")
sale_basket = (By.XPATH, "//div[@class='action-menu']/a[@id='sale-basket-basket-line-container']")
# cards = (By.CSS_SELECTOR, ".item-buy.btn")
button_card = (By.XPATH, "//*[@id='bx_3966226736_1094_7e1b8e3524755c391129a9d7e6f2d206_add_basket_link']")
basket_count = (By.XPATH, "//span[@class='basket-count']")
catalog = (By.CSS_SELECTOR, 'div.multi-menu:nth-child(1) > a:nth-child(1)')
by_type_of_furniture_and_room = (By.CSS_SELECTOR, 'div.multi-menu:nth-child(1) > div:nth-child(2)')
tumby = (By.CSS_SELECTOR, 'div.column:nth-child(1) > a:nth-child(2)')
see_all = (By.CSS_SELECTOR, '.see_all')
