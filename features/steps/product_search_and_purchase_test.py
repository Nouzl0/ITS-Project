from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time

# [0] - Background
# ---------------------------------------------
@given('the user is on the OpenCart website')
def step_given_user_is_on_opencart_website(context):
    context.driver.get("http://opencart:8080/")


# [1] - Scenario: View iPhone Product Details - DONE
# ---------------------------------------------
@given('a user is on the home page')
def step_given_user_is_on_home_page(context):
    context.driver.get("http://opencart:8080/")
    assert context.driver.current_url == "http://opencart:8080/"

@when('the user selects the iPhone product')
def step_when_user_selects_iphone_product(context):
    context.driver.find_element(By.CSS_SELECTOR, ".col:nth-child(2) .img-fluid").click()

@then('the user should see the iPhone product page')
def step_then_user_sees_iphone_product_page(context):
    assert context.driver.current_url == "http://opencart:8080/en-gb/product/iphone"

# [2] - Scenario: View Product Images - DONE
# [3] - Scenario: Add the Product to the Cart
# ---------------------------------------------
# [2], [3],
@given('a user is on the iPhone product page')
def step_given_user_is_on_iphone_product_page(context):
    context.driver.get("http://opencart:8080/en-gb/product/iphone")
    assert context.driver.current_url == "http://opencart:8080/en-gb/product/iphone"

# [2] 
@when('user clicks on the product image')
def step_when_user_clicks_on_product_image(context):
    context.driver.find_element(By.CSS_SELECTOR, "a > .mb-3").click()

@then('user should see more detailed product picture')
def step_then_user_sees_detailed_product_picture(context):
    assert context.driver.find_element(By.CLASS_NAME, "mfp-img")

# [3]
@when('the user adds the product to the cart')
def step_when_user_adds_product_to_cart(context):
    context.driver.find_element(By.ID, "button-cart").click()

# [3], [8]
@then('the user should see the product in the cart')
def step_then_user_sees_product_in_cart(context):
    assert context.driver.find_element(By.XPATH, "/html/body/div/div")

# [4] - Scenario Outline: Search for a MacBook 
# ---------------------------------------------
@given('a user is on the site')
def step_given_user_is_on_the_site(context):
    websites = ["http://opencart:8080/en-gb/product/iphone", 
                "http://opencart:8080/",
                "http://opencart:8080/en-gb/product/tablet/samsung-galaxy-tab-10-1",
                "http://opencart:8080/en-gb?route=checkout/cart"]
    chosen_website = random.choice(websites)
    context.driver.get(chosen_website)

@when('the user searches for a MacBook')
def step_when_user_searches_for_macbook(context):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("MacBook")
    context.driver.find_element(By.NAME, "search").send_keys(Keys.ENTER)

@then('the user should see related search results for MacBook')
def step_then_user_sees_related_search_results_for_macbook(context):
    assert context.driver.find_element(By.ID, "product-list")

# [5] - Scenario: Filter Search Results
# [6] - Scenario: Add Products to Comparison List
# ---------------------------------------------
# [5], [6]
@given('the user is on the search results page for Macbook')
def step_given_user_is_on_search_results_page_for_macbook(context):
    step_when_user_searches_for_macbook(context)
    assert context.driver.find_element(By.ID, "product-list")

# [5]
@when('user filters search results by price from high to low')
def step_when_user_filters_search_results_by_price_from_high_to_low(context):
    context.driver.find_element(By.ID, "input-sort").click()
    dropdown = context.driver.find_element(By.ID, "input-sort")
    dropdown.find_element(By.XPATH, "//option[. = 'Price (High > Low)']").click()

@then('the user should see the search results ordered by price')
def step_then_user_sees_search_results_ordered_by_price(context):
    price_elements = context.driver.find_elements(By.CSS_SELECTOR, ".product-thumb .price-new")
    prices = [float(price.text.replace('$', '').replace(',', '')) for price in price_elements]
    assert prices == sorted(prices, reverse=True), "Prices are not sorted from highest to lowest"

# [6]
@when('the user selects the ("Macbook Pro", "Macbook Air") products to be compared')
def step_when_user_selects_products_to_be_compared(context):
    element1 = context.driver.find_element(By.CSS_SELECTOR, ".col:nth-child(2) button[title='Compare this Product']")
    context.driver.execute_script("arguments[0].click();", element1)

    element2 = context.driver.find_element(By.CSS_SELECTOR, ".col:nth-child(3) button[title='Compare this Product']")
    context.driver.execute_script("arguments[0].click();", element2)

@then('the user should see that the products are in the comparison list')
def step_then_user_sees_products_in_comparison_list(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".alert")


# [7] - Scenario: Compare Products
# ---------------------------------------------
@given('a user has products in comparison list')
def step_given_user_has_products_in_comparison_list(context):
    step_when_user_searches_for_macbook(context)

@when('the user clicks on the compare button')
def step_when_user_clicks_on_compare_button(context):
    context.driver.find_element(By.ID, "compare-total").click()

@then('user should see the comparison page')
def step_then_user_sees_comparison_page(context):
    context.driver.get("http://opencart:8080/en-gb?route=product/compare")
    assert context.driver.current_url == "http://opencart:8080/en-gb?route=product/compare"


# [8] - Scenario: Add Cheapest Compared Product to Cart
# ---------------------------------------------
@given('the user is comparing products')
def step_given_user_is_comparing_products(context):
   step_then_user_sees_comparison_page(context)

@when('the user adds the cheapest product to the cart')
def step_when_user_adds_cheapest_product_to_cart(context):
    context.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/table/tbody[2]/tr/td[2]/form/button").click()

# [9] - Scenario: Proceed to Checkout
# ---------------------------------------------
@given('the user has products in the cart')
def step_given_user_has_products_in_cart(context):
    context.driver.get("http://opencart:8080/")

@given('the user has clicked on the cart preview')
def step_given_user_has_clicked_on_cart_preview(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn-inverse").click()
    assert context.driver.find_element(By.CSS_SELECTOR, ".text-end:nth-child(4)")

@when('the user selects the checkout option')
def step_when_user_selects_checkout_option(context):
    context.driver.find_element(By.CSS_SELECTOR, "a:nth-child(2) > strong").click()

@then('the user should see the checkout page')
def step_then_user_sees_checkout_page(context):
    assert context.driver.current_url == "http://opencart:8080/en-gb?route=checkout/checkout"

# [10] - Scenario: Complete Purchase
# ---------------------------------------------
@given('a user is on the checkout page')
def step_given_user_is_on_checkout_page(context):
    context.driver.get("http://opencart:8080/en-gb?route=checkout/checkout")

@when('the user fills payment information')
def step_when_user_fills_payment_information(context):
    context.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[1]/div[1]/div[2]/input").click()
    context.driver.find_element(By.ID, "input-firstname").click()
    context.driver.find_element(By.ID, "input-firstname").send_keys("adfsdf")
    context.driver.find_element(By.ID, "input-lastname").click()
    context.driver.find_element(By.ID, "input-lastname").send_keys("asddfasdff")
    context.driver.find_element(By.ID, "input-shipping-company").click()
    context.driver.find_element(By.ID, "input-shipping-company").send_keys("asdadsf")
    context.driver.find_element(By.ID, "input-shipping-address-1").click()
    context.driver.find_element(By.ID, "input-shipping-address-1").send_keys("asdfadsafs")
    context.driver.find_element(By.ID, "input-shipping-address-2").click()
    context.driver.find_element(By.ID, "input-shipping-address-2").send_keys("asdfadsf")
    context.driver.find_element(By.ID, "input-email").click()
    context.driver.find_element(By.ID, "input-email").send_keys("asdadsf@dsadasf.com")
    context.driver.find_element(By.ID, "input-shipping-city").click()
    context.driver.find_element(By.ID, "input-shipping-city").send_keys("adsffadsf")
    context.driver.find_element(By.ID, "input-shipping-postcode").click()
    context.driver.find_element(By.ID, "input-shipping-postcode").send_keys("adsffdsfs")
    context.driver.find_element(By.ID, "input-shipping-country").click()
    dropdown = context.driver.find_element(By.ID, "input-shipping-country")
    dropdown.find_element(By.XPATH, "//option[. = 'Tuvalu']").click()
    dropdown = context.driver.find_element(By.ID, "input-shipping-zone")
    dropdown.find_element(By.XPATH, "//option[. = 'Niulakita']").click()
    context.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[1]/div/form/div[2]/div/button").click()
    context.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[2]/div[1]/fieldset/div[1]/button").click()
    context.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[2]/div[2]/fieldset/div[1]/button").click()
    context.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[2]/div[3]/div[2]/div/button").click()

@when('confirms the purchase')
def step_when_user_confirms_purchase(context):
    # Transaction is incompleteble
    assert context.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[2]/div[3]/div[2]/div/button")
    context.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[2]/div[3]/div[2]/div/button").click()
    
@then('the user should receive confirmation of the purchase')
def step_then_user_receives_confirmation_of_purchase(context):
    # Transaction is incompleteble
    assert context.driver.current_url == "http://opencart:8080/en-gb?route=checkout/checkout/success"