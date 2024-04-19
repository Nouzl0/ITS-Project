from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time

# [18] - Background
# ---------------------------------------------
@given('the user is on the OpenCart administration website')
def step_given_user_is_on_opencart_admin_website(context):
    pass

@given('the user is logged in as an admin')
def step_given_user_is_logged_in_as_admin(context):
    pass


# [19] - Scenario: Navigation in the Catalog Menu
# ---------------------------------------------
@given('a user just logged in')
def step_given_user_just_logged_in(context):
    pass

@when('the user navigates to the Catalog menu')
def step_when_user_navigates_to_catalog_menu(context):
    pass

@when('selects a sub-menu')
def step_when_user_selects_a_sub_menu(context):
    pass

@then('the user should be redirected to the corresponding page')
def step_then_user_is_redirected_to_corresponding_page(context):
    pass


# [20] - Scenario Outline: Edit a Specific Category
# ---------------------------------------------
@given('a user is on the Categories page')
def step_given_user_is_on_categories_page(context):
    pass

@when('the user searches for the "{category}"')
def step_when_user_searches_for_category(context, category):
    pass

@when('clicks on the Edit action button')
def step_when_user_clicks_on_edit_action_button(context):
    pass

@then('the user should be redirected to the category edit page')
def step_then_user_is_redirected_to_category_edit_page(context):
    pass


# [21] - Scenario: Modify Category Information
# ---------------------------------------------
@given('the user is on the category edit page')
def step_given_user_is_on_category_edit_page(context):
    pass

@given('navigates to the General tab')
def step_given_user_navigates_to_general_tab(context):
    pass

@when('the user changes the category information')
def step_when_user_changes_category_information(context):
    pass

@then('the category information should be updated')
def step_then_category_information_should_be_updated(context):
    pass


# [22] - Scenario: Delete a Category
# ---------------------------------------------
@given('a user is on the Categories page')
def step_given_user_is_on_categories_page(context):
    pass

@when('the user deletes a selected category')
def step_when_user_deletes_selected_category(context):
    pass

@then('the category should be removed')
def step_then_category_should_be_removed(context):
    pass


# [24] - Scenario Outline: Edit a Specific Product
# ---------------------------------------------
@given('a user is on the Products page')
def step_given_user_is_on_products_page(context):
    pass

@when('the user searches for the "{product}"')
def step_when_user_searches_for_product(context, product):
    pass

@when('clicks on the Edit action button')
def step_when_user_clicks_on_edit_action_button(context):
    pass

@then('the user should be redirected to the product edit page')
def step_then_user_is_redirected_to_product_edit_page(context):
    pass

# [25] - Scenario: Change the Product Data
# ---------------------------------------------
@given('a user is in the product edit page')
def step_given_user_is_in_product_edit_page(context):
    pass

@given('navigates to the Data tab')
def step_given_user_navigates_to_data_tab(context):
    pass

@when('the user changes the product data')
def step_when_user_changes_product_data(context):
    pass

@then('the product data should be updated')
def step_then_product_data_should_be_updated(context):
    pass

# [26] - Scenario: Start creating a new product
# ---------------------------------------------
@given('the user is on the Products page')
def step_given_user_is_on_products_page(context):
    pass

@when('the user clicks on the Add button')
def step_when_user_clicks_on_add_button(context):
    pass

@then('the user should be redirected to the product add page')
def step_then_user_is_redirected_to_product_add_page(context):
    pass

# [27] - Scenario: Add a new product
# ---------------------------------------------
@given('the user is on the product add page')
def step_given_user_is_on_product_add_page(context):
    pass

@when('the user fills the product information')
def step_when_user_fills_product_information(context):
    pass

@when('selects a category')
def step_when_user_selects_a_category(context):
    pass

@then('the product should be added to the selected category')
def step_then_product_should_be_added_to_selected_category(context):
    pass