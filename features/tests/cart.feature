Feature: Tests for Cart functionality

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target home page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown

  Scenario: Add a product to the cart
    Given Open target home page
    When I search for toothpaste
    And Click on Add to Cart button
    And Store product name
    And Click Add to Cart button from side navigation
    Then Open the cart page
    And Verify cart has toothpaste
    And Verify my cart has 1 item(s)




