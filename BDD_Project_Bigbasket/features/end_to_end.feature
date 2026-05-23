Feature: BigBasket End To End Scenario

  Scenario: Complete electronics product checkout flow
    When user clicks on login button
    And user enters valid mobile number from csv
    And user clicks on continue button
    And user waits for manual OTP entry
    And user clicks on verify button
    And user handles got it popup

    And user clicks on shop by category
    And user clicks on electronics category
    And user clicks on audio devices
    And user clicks on earbuds category

    And user adds first earbud two times

    And user clicks on brands filter
    And user selects boAt brand
    And user clicks on add button

    And user opens basket
    And user increments product quantity
    And user clicks on checkout button

    Then checkout page should be opened