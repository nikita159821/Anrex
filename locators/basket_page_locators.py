from selenium.webdriver.common.by import By

input_full_name = (By.CSS_SELECTOR, 'div.input-field[data-property-id-row="1"] label')
input_delivery_city = (By.CSS_SELECTOR, 'div.input-field[data-property-id-row="2"] label')
input_street = (By.CSS_SELECTOR, 'div.input-field[data-property-id-row="3"] label')
input_house = (By.CSS_SELECTOR, 'div.input-field[data-property-id-row="4"] label')
input_body = (By.CSS_SELECTOR, 'div.input-field[data-property-id-row="5"] label')
input_flat = (By.CSS_SELECTOR, 'div.input-field[data-property-id-row="6"] label')
input_phone_number = (By.CSS_SELECTOR, 'div.input-field[data-property-id-row="7"] label')
input_mail = (By.CSS_SELECTOR, 'div.input-field[data-property-id-row="8"] label')
input_your_comment = (By.CSS_SELECTOR, '.bx-soa-customer-label')
button_basket = (By.XPATH, '//div[@class="action-menu d-none d-sm-flex")]/id[@id="sale-basket-basket-line-container"]')
placeholder_name = (By.XPATH, "//input[@id='soa-property-1'][@placeholder='Антон Иванов']")
placeholder_address = (By.XPATH, "//input[@id='soa-property-2'][@placeholder='Москва']")
placeholder_street = (By.XPATH, "//input[@id='soa-property-3'][@placeholder='Проспект Ленина']")
placeholder_house = (By.XPATH, "//input[@id='soa-property-4'][@placeholder='10']")
placeholder_building = (By.XPATH, "//input[@id='soa-property-5'][@placeholder='2Б']")
placeholder_apartment = (By.XPATH, "//input[@id='soa-property-6'][@placeholder='200']")
placeholder_phone = (By.XPATH, "//input[@id='soa-property-7'][@placeholder='+ 7 (999) 000-00-00']")
placeholder_email = (By.XPATH, "//input[@id='soa-property-8'][@placeholder='ivanova@yandex.ru']")
placeholder_comment = (By.XPATH, "//textarea[@id='orderDescription']")
name_input_send_keys = (By.CSS_SELECTOR, '#soa-property-1')
input_delivery_city_send_keys = (By.CSS_SELECTOR, '#soa-property-2')
input_street_send_keys = (By.CSS_SELECTOR, '#soa-property-3')
input_house_send_keys = (By.CSS_SELECTOR, '#soa-property-4')
input_body_send_keys = (By.CSS_SELECTOR, '#soa-property-5')
input_flat_send_keys = (By.CSS_SELECTOR, '#soa-property-6')
input_phone_number_send_keys = (By.CSS_SELECTOR, '#soa-property-7')
input_mail_send_keys = (By.CSS_SELECTOR, '#soa-property-8')
input_your_comment_send_keys = (By.XPATH, "//textarea[@id='orderDescription']")
button_arrange_order = (By.CSS_SELECTOR, '#bx-soa-total > div > div.bx-soa-cart-total-button-container > a')
order_confirmation = (By.XPATH, "//h2[text()='Подтверждение заказа']")
error_name = (By.CSS_SELECTOR, '#tooltip-soa-property-1 .tooltip-inner')