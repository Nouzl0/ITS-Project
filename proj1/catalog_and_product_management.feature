Feature: Catalog and Product Management

  Background:
    Given the user is on the OpenCart administration website
    And the user is logged in as an admin

  Scenario: Navigation in the Catalog Menu
    Given a user just logged in
    When the user navigates to the Catalog menu
    And selects a sub-menu
    Then the user should be redirected to the corresponding page 

  Scenario Outline: Edit a Specific Category
    Given a user is on the Categories page
    When the user searches for the "<category>"
    And clicks on the Edit action button
    Then the user should be redirected to the category edit page

    Examples:
      | category              |
      | Desktops              |
      | Cameras               |
      | Laptops & Notebooks   |

  Scenario: Modify Category Information
    Given the user is on the category edit page
    And navigates to the General tab
    When the user changes the category information
    Then the category information should be updated

  Scenario: Delete a Category
    Given a user is on the Categories page
    When the user deletes a selected category
    Then the category should be removed

  Scenario Outline: Edit a Specific Product
    Given a user is on the Products page
    When the user searches for the "<product>"
    And clicks on the Edit action button
    Then the user should be redirected to the product edit page

    Examples:
      | product       |
      | iMac          |
      | MacBook       |
      | MacBook Air   |
      | MacBook Pro   |
    
  Scenario: Change the Product Data
    Given a user is in the product edit page
    And navigates to the Data tab
    When the user changes the product data
    Then the product data should be updated

  Scenario: Start creating a new product
    Given the user is on the Products page
    When the user clicks on the Add button
    Then the user should be redirected to the product add page
    
  Scenario: Add a new product
    Given the user is on the product add page
    When the user fills the product information 
    And selects a category
    Then the product should be added to the selected category