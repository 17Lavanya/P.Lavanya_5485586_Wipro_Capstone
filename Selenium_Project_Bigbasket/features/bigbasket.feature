Feature: BigBasket electronics automation

  Background:
    Given user launches the BigBasket website

  Scenario: Login with valid mobile number from CSV
    When user logs in using mobile number from CSV
    Then user should be on the BigBasket website

  Scenario: Open electronics category
    When user logs in using mobile number from CSV
    And user opens the electronics category
    Then electronics category should be displayed

  Scenario: Apply boAt brand filter for earbuds
    When user logs in using mobile number from CSV
    And user opens earbuds under electronics audio devices
    And user applies the boAt brand filter
    Then brand filter should be applied successfully

  Scenario: Add boAt earbuds product to basket
    When user logs in using mobile number from CSV
    And user opens earbuds under electronics audio devices
    And user applies the boAt brand filter
    And user adds product to basket
    Then basket should be opened

  Scenario: Complete BigBasket electronics end to end flow
    When user logs in using mobile number from CSV
    And user completes the electronics checkout flow
    Then checkout page should be displayed

  Scenario: Validate invalid mobile number
    When user enters invalid mobile number "12345"
    Then continue button should be disabled

  Scenario: Validate invalid OTP login
    When user starts login using mobile number from CSV
    And user verifies without valid OTP
    Then invalid OTP flow should be handled
