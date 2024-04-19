# Report proj2-xnosal01
**Author** - Nikolas Nosal, xnosal01, xnosal01@stud.fit.vutbr.cz
**Date** - 19/04/2024
**Reason** - BugReport

## Bug Report

**Title**: User can't choose payment method

**Reported by**: Nikolas Nosal, xnosal01, xnosal01@stud.fit.vutbr.cz

**Date**: 19/04/2024

**Description**: When the user reaches the checkout page and tries to select a payment method, no options are available. This prevents the user from completing the purchase.

**Steps to reproduce**:
1. Navigate to the OpenCart website.
2. Add a product to the cart.
3. Proceed to the checkout page.
4. Fill out requested user information.
5. Try to select a payment method.

**Expected result**: The user should be able to select a payment method and complete the purchase.

**Actual result**: No payment methods are available for selection.

**OS**: Windows 11, 23H2 (22631)

**Browser**: Chrome 111.0

**Test Case**
```gherkin
Scenario: Complete Purchase                                 
  Given the user is on the OpenCart website                 
  And a user is on the checkout page                      
  When the user fills payment information                   
  And confirms the purchase                                 
  Then the user should receive confirmation of the purchase 
```

**Test Log**
```behave
  Scenario: Complete Purchase                                 # product_search_and_purchase.feature:58
    Given the user is on the OpenCart website                 # steps/product_search_and_purchase_test.py:9
    Given a user is on the checkout page                      # steps/product_search_and_purchase_test.py:161
    When the user fills payment information                   # steps/product_search_and_purchase_test.py:165
    And confirms the purchase                                 # None
    Then the user should receive confirmation of the purchase # None
```