Feature: Tests to verify Header UI elements
@smoke
  Scenario: Verify header has expected amount of links
    Given Open target home page
    Then Verify header has 6 links

    #Target circle
  Scenario: Verify there are benefit cells
    Given Open target home page
    When Click on 'Target Circle' button
    Then Verify page has at least 3 benefits cells