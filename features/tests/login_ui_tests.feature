Feature: Tests for Target Legal pages

  Scenario: User is able to open Privacy Policy
    Given Open target login page
    And Store original window
    When Click Privacy Policy link
    And Switch to new window
    Then Verify Privacy Policy page opened
    And Close current window
    And Return to original window