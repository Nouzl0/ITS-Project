from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

driver = None

@given('the user is on the OpenCart website')
def step_given_user_is_on_opencart_website(context):
    global driver
    driver = webdriver.Firefox()
    driver.get("http://localhost/")

@given('a user is on the home page')
def step_given_user_is_on_home_page(context):
    # Assuming that the OpenCart website is the home page
    assert driver.current_url == "http://localhost/"

@when('the user selects the iPhone product')
def step_when_user_selects_iphone_product(context):
    # Find the iPhone product and click on it
    iphone_product = driver.find_element_by_link_text('iPhone')
    iphone_product.click()

@then('the user should see the iPhone product page')
def step_then_user_sees_iphone_product_page(context):
    # Check that the current URL is the iPhone product page URL
    assert 'iphone' in driver.current_url.lower()
    driver.quit()