Feature: Items can be added to the cart and represented in the cart

  Scenario: Add a product to the cart and verify it is present
    Given Open target home page
    When I search for toothpaste
    And Click on Add to Cart button
    And Click Add to Cart button from side navigation
    Then Open the cart page
    And Verify cart has toothpaste
    And Verify my cart has 1 item(s)





