from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import random


# [11] - Background: User is logged in
# ---------------------------------------------
@given('the user is logged in')
def step_given_user_is_logged_in(context):
    context.driver.get("http://opencart:8080/en-gb?route=account/register")
    
    # Register a new user if not logged in
    if (context.driver.current_url == "http://opencart:8080/en-gb?route=account/register"):
        context.driver.find_element(By.ID, "input-firstname").click()
        context.driver.find_element(By.ID, "input-firstname").send_keys(context.first_name)
        context.driver.find_element(By.ID, "input-lastname").click()
        context.driver.find_element(By.ID, "input-lastname").send_keys(context.last_name)
        context.driver.find_element(By.ID, "input-email").click()
        context.driver.find_element(By.ID, "input-email").send_keys(context.email)
        context.driver.find_element(By.ID, "input-password").click()
        context.driver.find_element(By.ID, "input-password").send_keys(context.password)
        context.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/div/div/input").click()
        context.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/form/div/button").click()

    context.driver.get("http://opencart:8080/")
# [12] - Scenario: Searching for category monitor or display
# ---------------------------------------------
@when('the user searches for monitors in the category Components->Monitors')
def step_when_user_searches_for_monitors(context):
    context.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/a").click()
    context.driver.find_element(By.XPATH, "/html/body/main/div[1]/nav/div[2]/ul/li[3]/div/div/ul/li[2]/a").click()

@then('they should see a list of monitors')
def step_then_user_sees_list_of_monitors(context):
    assert context.driver.current_url == "http://opencart:8080/en-gb/catalog/component/monitor"


# [12] - Scenario: Add Samsung Monitor to Wish List
# ---------------------------------------------
@given('a user is on the monitor search results page')
def step_given_user_is_on_monitor_search_results_page(context):
    context.driver.get("http://opencart:8080/en-gb/catalog/component/monitor")

@when('the user adds a Samsung monitor to the wish list')
def step_when_user_adds_samsung_monitor_to_wish_list(context):
    context.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[3]/div[2]/div/div[2]/form/div/button[2]").click()

@then('they should see that the Samsung monitor is added to their wish list')
def step_then_user_sees_samsung_monitor_in_wish_list(context):
    assert context.driver.find_element(By.XPATH, "/html/body/div/div")


# [13] - Scenario: Viewing the Wish List
# ---------------------------------------------
@given('a user has added {product} to their wish list')
def step_given_user_has_added_product_to_wish_list(context, product):
    text = context.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[3]/a").text
    if text == "Wish List (0)": 
        assert False

@when('the user views the wish list')
def step_when_user_views_wish_list(context):
    context.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[3]/a").click()

@then('they should see the {product} in wish list page')
def step_then_user_sees_product_in_wish_list_page(context, product):
    assert context.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div")


# [14] - Scenario: Add Samsung Monitor to Cart
# ---------------------------------------------
@given('the user has a Samsung Monitor in their wish list')
def step_given_user_has_samsung_monitor_in_wish_list(context):
    context.driver.get("http://opencart:8080/")
    context.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[3]/a").click()
    assert context.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div")

@when('the user adds the Samsung monitor to the cart')
def step_when_user_adds_samsung_monitor_to_cart(context):
    context.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/table/tbody/tr/td[6]/form/button[1]").click()

@then('they should see that the Samsung monitor is in their cart page')
def step_then_user_sees_samsung_monitor_in_cart_page(context):
    assert context.driver.find_element(By.XPATH, "/html/body/div/div")


# [15] - Scenario: Add Samsung Monitor to Cart
# ---------------------------------------------
@given('the user has added a product to their cart')
def step_given_user_has_added_product_to_cart(context):
    context.driver.get("http://opencart:8080/")
    context.driver.find_element(By.CSS_SELECTOR, ".btn-inverse").click()
    assert context.driver.find_element(By.CSS_SELECTOR, ".text-end:nth-child(4)")

@when('the user selects the "View Cart" option')
def step_when_user_selects_view_cart_option(context):
    context.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[4]/a").click()

@then('they should see the product in their cart')
def step_then_user_sees_product_in_cart(context):
    assert context.driver.current_url == "http://opencart:8080/en-gb?route=checkout/cart"

# [16] - Scenario: Add Samsung Monitor to Cart
# ---------------------------------------------
@given('a user is on the cart page with a product in their cart')
def step_given_user_is_on_cart_page_with_product(context):
    context.driver.get("http://opencart:8080/en-gb?route=checkout/cart")

@when('the user removes the product from their cart')
def step_when_user_removes_product_from_cart(context):
    context.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[1]/div/table/tbody/tr/td[4]/form/div/button[2]").click()

@then('they should not see the product in their cart anymore')
def step_then_user_does_not_see_product_in_cart(context):
    assert context.driver.find_element(By.XPATH, "/html/body/div/div")