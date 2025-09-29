
Feature: Test login page

  Scenario: Verify user is directed to login page
    Given Open target home page
    When Click the account button sign in button opens
    Then Click sign in button
    Then Verify 'Sign in or create account' text


  Scenario: Verify user can sign in
    Given Open target home page
    When Click the account button sign in button opens
    Then Click sign in button
    And Enter user morvitalgr@edgetopgrid.com
    And Click sign in by password button
    And Enter password Testers1
    Then Verify ***** is signed in


  Scenario: Verify user gets error for incorrect password
    Given Open target home page
    When Click the account button sign in button opens
    Then Click sign in button
    And Enter user morvitalgr@edgetopgrid.com
    And Click sign in by password button
    And Enter password Testers2
    Then Verify password error message is shown
