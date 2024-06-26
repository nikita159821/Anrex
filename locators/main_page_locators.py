from selenium.webdriver.common.by import By

logo = (By.XPATH, '//img[@class="logo d-block"]')
city = (By.CLASS_NAME, 'city_wrap')
popup_city = (By.XPATH, "//h3[text()='Выберите Ваш регион']")
close = (By.XPATH, "//button[@class='callback-close popup-close']")
search = (By.XPATH, "//a[@class='action']")
search_active = (By.XPATH, "//a[@class='action active']")
slider = (By.XPATH, "//div[@class='row header_top']")
first_city = (By.XPATH, "//ul[@class='city_list']/li[1]")
callback_link = (By.XPATH, "//a[@class='callback-link d-none d-md-block']")
hover_text = (By.CSS_SELECTOR, "a.callback-link > span")
title_back_call = (By.XPATH, "//h3[contains(., 'Заявка на обратный')]")
text_back_call = (By.XPATH, "//p[@class='text-center']")
input_name = (By.XPATH, "//input[@id='callback_name']")
input_phone = (By.XPATH, "//input[@id='callback_phone']")
name_placeholder = (By.CSS_SELECTOR, '[placeholder="Антон"]')
phone_placeholder = (By.CSS_SELECTOR, '[placeholder="+7 (960) 345-44-19"]')
name_error = (By.XPATH, "//div[@class='align-items-center d-flex flex-column input-field has-error']")
phone_error = (By.XPATH, "//div[@class='align-items-center d-flex flex-column input-field has-error']")
email_error = (By.XPATH, "//div[@class='form-control input-field form-control-plaintext has-error']")
title_sale = (By.XPATH, "//b[text()='Товары со скидками']")
title_popular = (By.XPATH, "//b[text()='Популярные категории']")
button_send_application = (By.XPATH, "//input[@id='callback_submit']")
popup_back_call = (By.XPATH, "//p[contains(text(), 'Ваша заявка была направлена')]")
tel_callback = (By.ID, 'tel-callback')
search_cvg = (By.CSS_SELECTOR, ".action > svg:nth-child(1)")
search_line = (By.XPATH, "//div[@class='search']")
search_line_close = (By.XPATH, "//div[@class='search d-sm-none']")
sale_basket = (By.XPATH, "//div[@class='action-menu d-none d-sm-flex']/a[@id='sale-basket-basket-line-container']")
# cards = (By.CSS_SELECTOR, ".item-buy.btn")
button_card = (By.XPATH, "//div[@class='item-actions 123']")
basket_count = (By.XPATH, "//span[@class='basket-count']")
catalog = (By.CSS_SELECTOR, 'div.multi-menu:nth-child(1) > a:nth-child(1)')
by_type_of_furniture_and_room = (By.CSS_SELECTOR, 'div.multi-menu:nth-child(1) > div:nth-child(2)')
tumby = (By.CSS_SELECTOR, 'div.column:nth-child(1) > a:nth-child(2)')
see_all = (By.CSS_SELECTOR, '.see_all')
collections = (By.CSS_SELECTOR, '.menu > a:nth-child(2)')
delivery = (By.CSS_SELECTOR, 'div.multi-menu:nth-child(3) > a:nth-child(1)')
delivery_list = (By.CSS_SELECTOR, 'div.multi-menu:nth-child(3) > div:nth-child(2)')
delivery_dropdown = (By.CSS_SELECTOR, 'div.multi-menu:nth-child(3) > div:nth-child(2) > a:nth-child(1)')
guarantee = (By.CSS_SELECTOR, 'div.multi-menu:nth-child(3) > div:nth-child(2) > a:nth-child(2)')
shops = (By.CSS_SELECTOR, 'div.multi-menu:nth-child(3) > div:nth-child(2) > a:nth-child(3)')
sale = (By.CSS_SELECTOR, '.menu > a:nth-child(4)')
about = (By.CSS_SELECTOR, 'div.multi-menu:nth-child(6) > a:nth-child(1)')
about_list = By.CSS_SELECTOR, 'div.multi-menu:nth-child(6) > div:nth-child(2)'
about_dropdown = (By.CSS_SELECTOR, 'div.multi-menu:nth-child(6) > div:nth-child(2) > a:nth-child(1)')
dealers_dropdown = (By.CSS_SELECTOR, 'div.multi-menu:nth-child(6) > div:nth-child(2) > a:nth-child(2)')
contact_dropdown = (By.CSS_SELECTOR, 'div.multi-menu:nth-child(6) > div:nth-child(2) > a:nth-child(3)')
discounted_products = (By.CSS_SELECTOR, '.good_list')
button_card_discounted = (By.CSS_SELECTOR, 'div.catalog-item:nth-child(7) > div:nth-child(5)')
popular_categories = (By.XPATH, "//section[@class='index-sections']")
popular_section_banner = (By.CSS_SELECTOR, 'div.section_banner-item:nth-child(1) > a:nth-child(1)')
banner_slider = (By.XPATH, "//section[@class='index-banner d-none d-sm-block']")
button_up = (By.XPATH, "//button[@class='banner-prev']")
button_down = (By.XPATH, "//button[@class='banner-next']")
slider_gostinie = (By.CSS_SELECTOR, 'p.active > a:nth-child(1)')
slider_kabineti = (By.CSS_SELECTOR, 'p.active > a:nth-child(1)')
carousel_title = (By.XPATH, "//h2[text()='Мебель для']")
img = (By.CSS_SELECTOR, '.index-banner-image')
section_collections = (By.CSS_SELECTOR, '.index-collections')
button_right = (By.XPATH, "//div[@class='slider-arrow next slick-arrow']")
button_left = (By.XPATH, "//div[@class='slider-arrow prev slick-arrow']")
collections_title_jazz = (By.XPATH, "//h4[text()='Коллекция «Джаз»']")
collections_title_valencia = (By.XPATH, "//h4[text()='Коллекция «Валенсия»']")
button_collections = (By.XPATH, "//h4[text()='Коллекция «Джаггер»']/following-sibling::span[@class='btn btn-success']")
view_collections = (By.CSS_SELECTOR, '.collections_slider_wrap > div:nth-child(3) > a:nth-child(1)')
reviews = (By.XPATH, "//section[@class='index-reviews']")
review_cards = (By.CSS_SELECTOR, '.reviews-wrap .review-item')
review_card = (By.CSS_SELECTOR, '.reviews-wrap .review-item')
# Получение имени автора отзыва
name = (By.XPATH, '//div[contains(@class, "review-item")]/h4[text()="Светлана"]')
# Получение даты отзыва
date = (By.XPATH, '//span[text()="15.04.2024"]')
# Получение текста отзыва
content = (By.XPATH, '//div[@class="review-content" and contains(text(), "Спасибо команде доставщиков!")]')
stars = (By.CSS_SELECTOR, '.review-stars .stars')
read_more_link = (By.CSS_SELECTOR, 'span.read_more > a.btn-link')
review_popup = (By.CSS_SELECTOR, 'div.popup-box > div.review_popup')
popup_close_review = (By.CSS_SELECTOR, '#review-item > div.popup-box > button.callback-close.popup-close')
review_item = (By.XPATH, "//*[@id='review-item']")
review_button = (By.XPATH, "//a[@class='btn btn-default' and contains(text(), 'Смотреть все отзывы')]")
logo_footer = (By.XPATH, "//div[@class='form-callback-wrap']/img[@class='logo d-none d-sm-block']")
name_of_company = (By.CSS_SELECTOR, '.copyright')
text_comment = (By.XPATH, "//div[@class='form-callback']/p")
footer = (By.XPATH, "//div[@class='footer']")
button_write = (By.XPATH, "//div[@class='form-callback']/a")
title_form_feedback = (By.XPATH, "//h3[text()='Форма обратной связи']")
text_form_feedback = (By.XPATH, "//p[contains(., 'Напишите нам и поделитесь Вашим мнением о нас')]")
radio_buttons = (By.CSS_SELECTOR, "div.form-control-radio label")
form_close = (By.XPATH, "//div[@id='callback_form']/div/button")
form_overlay_close = (By.XPATH, "//div[@id='callback_form']")
input_name_form_feedback = (By.XPATH, "//input[@id='callback_form_name']")
input_phone_form_feedback = (By.XPATH, "//input[@id='callback_form_phone']")
input_email_form_feedback = (By.XPATH, '//input[@name="callback_form_email"]')
input_question_form_feedback = (By.XPATH, "//label[@for='callback_form_question']")
name_placeholder_form_feedback = (By.XPATH, "//input[@id='callback_form_name']")
phone_placeholder_form_feedback = (By.XPATH, "//input[@id='callback_form_phone']")
email_placeholder_form_feedback = (By.XPATH, '//input[@name="callback_form_email"]')
question_placeholder_form_feedback = (By.XPATH, "//textarea[@id='callback_form_question']")
button_form_feedback = (By.XPATH, "//input[@id='callback_form_submit']")
checkbox_radio_button = (By.XPATH, "//input[@id='callback_type_1']")
popup_form_feedback = (By.CSS_SELECTOR, "#callback_form-success > div:nth-child(1) > p:nth-child(3)")

