Feature: Elements on the Target Help page can be located

  Scenario: Verify elements on Target Help UI
    Given Open target home page
    When Click the account button sign in button opens
    Then Click the help center button
    And Verify Help page url
    And Verify 9 help tiles are on page

  Scenario: User can select Help Topic Promotions and coupons
    Given Open help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Promotions & Coupons
    Then Verify help Current promotions page opened

  Scenario: User can select Help Topic Gift Cards
    Given Open help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Gift Cards
    Then Verify help Target GiftCard balance page opened

  Scenario: User can select Help Topic Orders & Purchases
    Given Open help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Orders & Purchases
    Then Verify help Print a receipt page opened
