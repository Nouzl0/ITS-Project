Feature: Wish List and Cart Management

  Background:
    Given the user is on the OpenCart website
    And the user is logged in

  Scenario: Searching for category monitor or display
    Given a user is on the home page
    When the user searches for monitors in the category Components->Monitors
    Then they should see a list of monitors

  Scenario: Add Samsung Monitor to Wish List
    Given a user is on the monitor search results page
    When the user adds a Samsung monitor to the wish list
    Then they should see that the Samsung monitor is added to their wish list

  Scenario: Viewing the Wish List
    Given a user has added products to their wish list
    When the user views the wish list
    Then they should see the products in wish list page

  Scenario: Adding Samsung Monitor to the Cart from the Wish List
    Given the user has a Samsung Monitor in their wish list
    When the user adds the Samsung monitor to the cart
    Then they should see that the Samsung monitor is in their cart page

  Scenario: Viewing the Cart
    Given the user has added a product to their cart
    And the user has clicked on the cart preview
    When the user selects the "View Cart" option
    Then they should see the product in their cart

  Scenario: Removing a Product from the Cart
    Given a user is on the cart page with a product in their cart
    When the user removes the product from their cart
    Then they should not see the product in their cart anymore