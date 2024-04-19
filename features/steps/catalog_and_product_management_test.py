from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import string

# [18] - Background
# ---------------------------------------------
@given('the user is on the OpenCart administration website')
def step_given_user_is_on_opencart_admin_website(context):
    context.driver.get("http://opencart:8080/administration/")

@given('the user is logged in as an admin')
def step_given_user_is_logged_in_as_admin(context):
    context.driver.find_element(By.ID, "input-username").click()
    context.driver.find_element(By.ID, "input-username").send_keys(context.admin_username)
    context.driver.find_element(By.ID, "input-password").click()
    context.driver.find_element(By.ID, "input-password").send_keys(context.admin_password)
    context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div/div[2]/form/div[3]/button").click()

# [19] - Scenario: Navigation in the Catalog Menu
# ---------------------------------------------
@given('a user just logged in')
def step_given_user_just_logged_in(context):
    WebDriverWait(context.driver, 10).until(EC.url_changes("http://opencart:8080/administration/"))

@when('the user navigates to the Catalog menu')
def step_when_user_navigates_to_catalog_menu(context):
    context.driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[2]/a").click()
    
@when('selects a sub-menu')
def step_when_user_selects_a_sub_menu(context):
    context.driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[2]/ul/li[1]/a").click()

@then('the user should be redirected to the corresponding page')
def step_then_user_is_redirected_to_corresponding_page(context):
    text = context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/h1").text
    assert text == "Categories"


# [20] - Scenario Outline: Edit a Specific Category
# ---------------------------------------------
@given('a user is on the Categories page')
def step_given_user_is_on_categories_page(context):
    step_given_user_just_logged_in(context)
    step_when_user_navigates_to_catalog_menu(context)
    step_when_user_selects_a_sub_menu(context)

@when('the user searches for the "{category}"')
def step_when_user_searches_for_category(context, category):
    if (category == "Laptops & Notebooks"): 
        context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/form/div[2]/div[1]/ul/li[2]/a").click()
    elif category  in ["MacBook", "MacBook Air", "MacBook Pro"]:
        element = context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[2]/div[1]/ul/li[2]/a")
        context.driver.execute_script("arguments[0].scrollIntoView(); window.scrollBy(0, 180);", element)
        time.sleep(1)
        element.click()

    context.tmp_ref = category
    
@when('clicks on the Edit action button')
def step_when_user_clicks_on_edit_action_button(context):
    time.sleep(1)
    if (context.tmp_ref == "Desktops"):
        context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/form/div[1]/table/tbody/tr[10]/td[4]/a").click()
    elif (context.tmp_ref == "Cameras"):
        context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/form/div[1]/table/tbody/tr[1]/td[4]/a").click()
    elif (context.tmp_ref == "Laptops & Notebooks"):
        context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/form/div[1]/table/tbody/tr[3]/td[4]/a").click()
    elif (context.tmp_ref == "iMac"):
        context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[1]/table/tbody/tr[5]/td[7]/div/a").click()
    elif (context.tmp_ref == "MacBook"):
        context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[1]/table/tbody/tr[1]/td[7]/div/a").click()
    elif (context.tmp_ref == "MacBook Air"):
        context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[1]/table/tbody/tr[2]/td[7]/div/a").click()
    elif (context.tmp_ref == "MacBook Pro"):
        context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[1]/table/tbody/tr[3]/td[7]/div/a").click()

@then('the user should be redirected to the category edit page')
def step_then_user_is_redirected_to_category_edit_page(context):
    text = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/div/div[1]/div/div/div[1]/div/input").get_attribute("value")
    print(text)
    if (context.tmp_ref == "Desktops"):
        assert text == "Desktops"
    elif (context.tmp_ref == "Cameras"):
        assert text == "Cameras"
    elif (context.tmp_ref == "Laptops & Notebooks"):
        assert text == "Laptops & Notebooks"


# [21] - Scenario: Modify Category Information
# ---------------------------------------------
@given('the user is on the category edit page')
def step_given_user_is_on_category_edit_page(context):
    step_given_user_just_logged_in(context)
    step_when_user_navigates_to_catalog_menu(context)
    step_when_user_selects_a_sub_menu(context)
    context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/form/div[1]/table/tbody/tr[5]/td[4]/a").click()

@given('navigates to the General tab')
def step_given_user_navigates_to_general_tab(context):
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/ul/li[1]/a").click()

@when('the user changes the category information')
def step_when_user_changes_category_information(context):
    letters = string.ascii_lowercase
    context.tmp_ref = ''.join(random.choice(letters) for i in range(1))
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/div/div[1]/div/div/div[1]/div/input").send_keys(context.tmp_ref)
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/button").click()

@then('the category information should be updated')
def step_then_category_information_should_be_updated(context):
    assert context.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div")


# [22] - Scenario: Delete a Category
# ---------------------------------------------
@when('the user deletes a selected category')
def step_when_user_deletes_selected_category(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/form/div[2]/div[1]/ul/li[2]/a").click()
    time.sleep(1)
    context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/form/div[1]/table/tbody/tr[7]/td[1]/input").click()
    context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/button[2]").click()
    #context.driver.switch_to.alert.accept()
    context.driver.switch_to.alert.dismiss()
    pass

@then('the category should be removed')
def step_then_category_should_be_removed(context):
    #assert context.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div")
    pass
    

# [23] - Scenario Outline: Edit a Specific Product
# ---------------------------------------------
@given('a user is on the Products page')
def step_given_user_is_on_products_page(context):
    step_given_user_just_logged_in(context)
    step_when_user_navigates_to_catalog_menu(context)
    context.driver.find_element(By.XPATH, "/html/body/div/nav/ul/li[2]/ul/li[2]/a").click()

@then('the user should be redirected to the product edit page')
def step_then_user_is_redirected_to_product_edit_page(context):
    text = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/div/div[1]/div/div/div[1]/div/div[1]/input").get_attribute("value")
    if (context.tmp_ref == "iMac"):
        assert text == "iMac"
    elif (context.tmp_ref == "MacBook"):
        assert text == "MacBook"
    elif (context.tmp_ref == "MacBook Air"):
        assert text == "MacBook Air"
    elif (context.tmp_ref == "MacBook Pro"):
        assert text == "MacBook Pro"


# [24] - Scenario: Change the Product Data
# ---------------------------------------------
@given('a user is in the product edit page')
def step_given_user_is_in_product_edit_page(context):
    step_given_user_is_on_products_page(context)
    time.sleep(1)
    context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[1]/table/tbody/tr[4]/td[7]/div/a").click()

@given('navigates to the Data tab')
def step_given_user_navigates_to_data_tab(context):
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/ul/li[2]/a").click()

@when('the user changes the product data')
def step_when_user_changes_product_data(context):
    numbers = string.digits
    context.tmp_ref = ''.join(random.choice(numbers) for i in range(1))
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/div/div[2]/fieldset[3]/div[1]/div/input").clear()
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/div/div[2]/fieldset[3]/div[1]/div/input").send_keys(context.tmp_ref)
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/button").click()
   
@then('the product data should be updated')
def step_then_product_data_should_be_updated(context):
    assert context.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div")

# [26] - Scenario: Start creating a new product
# ---------------------------------------------
@given('the user is on the Products page')
def step_given_user_is_on_products_page(context):
    step_given_user_just_logged_in(context)
    step_when_user_navigates_to_catalog_menu(context)
    context.driver.find_element(By.XPATH, "/html/body/div/nav/ul/li[2]/ul/li[2]/a").click()

@when('the user clicks on the Add button')
def step_when_user_clicks_on_add_button(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div/div/a").click()

@then('the user should be redirected to the product add page')
def step_then_user_is_redirected_to_product_add_page(context):
    text = context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/h1").text
    assert text == "Products"

# [27] - Scenario: Add a new product
# ---------------------------------------------
@given('the user is on the product add page')
def step_given_user_is_on_product_add_page(context):
    step_given_user_is_on_products_page(context)
    step_when_user_clicks_on_add_button(context)


@when('the user fills the product information')
def step_when_user_fills_product_information(context):
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/div/div[1]/div/div/div[1]/div/div[1]/input").click()
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/div/div[1]/div/div/div[1]/div/div[1]/input").send_keys("New Product")
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/div/div[1]/div/div/div[3]/div/div[1]/input").click()
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/div/div[1]/div/div/div[3]/div/div[1]/input").send_keys("123456")
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/ul/li[2]/a").click() # Data tab
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/div/div[2]/fieldset[1]/div[1]/div/div[1]/input").click()
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/div/div[2]/fieldset[1]/div[1]/div/div[1]/input").send_keys("123456")
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/ul/li[11]/a").click() # Seo tab
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/div/div[11]/div[2]/table/tbody/tr/td[2]/div[1]/input").click()
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/div/div[11]/div[2]/table/tbody/tr/td[2]/div[1]/input").send_keys("new-product")

@when('selects a category')
def step_when_user_selects_a_category(context):
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/ul/li[3]/a").click() # Links tab
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/div/div[3]/div[2]/div/input").click()
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/form/div/div[3]/div[2]/div/input").send_keys("Components")
    
@then('the product should be added to the selected category')
def step_then_product_should_be_added_to_selected_category(context):
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/button").click()
    assert context.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div")