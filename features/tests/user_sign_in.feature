
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
    And Enter user ******
    And Click sign in by password button
    And Enter password *****
    Then Verify ***** is signed in
