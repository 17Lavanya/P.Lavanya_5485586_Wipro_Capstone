Feature: BigBasket Negative Scenarios

  Scenario: Validate invalid mobile number
    When user clicks on login button
    And user enters invalid mobile number "12121"
    Then continue button should be disabled

  Scenario: Validate invalid OTP
    When user clicks on login button
    And user enters valid mobile number from csv
    And user clicks on continue button
    And user waits for manual invalid OTP entry
    And user clicks on verify button
    Then invalid OTP error message should be displayed