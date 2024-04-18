Feature: Searching and buying products

  Background:
    Given the user is on the OpenCart website

  Scenario: View iPhone Product Details
    Given a user is on the home page
    When the user selects the iPhone product
    Then the user should see the iPhone product page

  Scenario: View Product Images
    Given a user is on the iPhone product page
    When user clicks on the product image
    Then user should see more detailed product picture

  Scenario: Add the Product to the Cart
    Given a user is on the iPhone product page
    When the user adds the product to the cart
    Then the user should see the product in the cart

  Scenario Outline: Search for a MacBook 
    Given a user is on the site
    When the user searches for a MacBook
    Then the user should see related search results for MacBook

    Examples:
      | related |
      | Macbook |
      | Macbook Pro |
      | Macbook Air |

  Scenario: Filter Search Results
    Given the user is on the search results page for Macbook
    When user filters search results by price from high to low
    Then the user should see the search results ordered by price

  Scenario: Add Products to Comparison List
    Given the user is on the search results page for Macbook
    When the user selects the ("Macbook Pro", "Macbook Air") products to be compared
    Then the user should see that the products are in the comparison list

  Scenario: Compare Products
    Given a user has products in comparison list
    When the user clicks on the compare button
    Then user should see the comparison page

  Scenario: Add Cheapest Compared Product to Cart
    Given the user is comparing products
    When the user adds the cheapest product to the cart
    Then the user should see the product in the cart

  Scenario: Proceed to Checkout
    Given the user has products in the cart
    And the user has clicked on the cart preview
    When the user selects the checkout option
    Then the user should see the checkout page

  Scenario: Complete Purchase
    Given a user is on the checkout page
    When the user fills payment information 
    And confirms the purchase
    Then the user should receive confirmation of the purchase