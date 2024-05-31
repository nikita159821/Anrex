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