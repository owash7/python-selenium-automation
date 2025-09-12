Feature: Tests for Target search functionality

  Scenario: User can search for a tea on Target
    Given Open target home page
    When I search for tea
    Then Verify search results are shown for tea

  Scenario: User can search for tea on target
   Given Open target home page
    When I search for iphone
    Then Verify search results are shown for iphone

  Scenario: User can search for tea on target
   Given Open target home page
    When I search for mug
    Then Verify search results are shown for mug

#  Scenario Outline: User can search for a product
#    Given Open target main page
#    When Search for <product>
#    Then Verify search results are shown for <expected_product>
#    Examples:
#    |product  |expected_product |
#    |iphone   |iphone           |
#    |coffee   |coffee           |
#    |tea      |tea              |
