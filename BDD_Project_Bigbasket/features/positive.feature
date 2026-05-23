Feature: BigBasket Positive Scenarios

  Scenario: Login with valid mobile number
    When user clicks on login button
    And user enters valid mobile number from csv
    And user clicks on continue button
    And user waits for manual OTP entry
    And user clicks on verify button
    Then user should be logged in successfully


  Scenario: Open electronics category
    When user clicks on login button
    And user enters valid mobile number from csv
    And user clicks on continue button
    And user waits for manual OTP entry
    And user clicks on verify button
    And user handles got it popup
    And user clicks on shop by category
    And user clicks on electronics category
    Then electronics category should be opened


  Scenario: Apply boAt brand filter
    When user clicks on login button
    And user enters valid mobile number from csv
    And user clicks on continue button
    And user waits for manual OTP entry
    And user clicks on verify button
    And user handles got it popup
    And user clicks on shop by category
    And user clicks on electronics category
    And user opens audio devices from positive flow
    And user opens earbuds category from positive flow
    And user clicks on brands filter
    And user selects boAt brand
    Then boAt brand filter should be applied successfully


  Scenario: Add product to basket
    When user clicks on login button
    And user enters valid mobile number from csv
    And user clicks on continue button
    And user waits for manual OTP entry
    And user clicks on verify button
    And user handles got it popup
    And user clicks on shop by category
    And user clicks on electronics category
    And user opens audio devices from positive flow
    And user opens earbuds category from positive flow
    And user clicks on brands filter
    And user selects boAt brand
    And user clicks on add button
    And user opens basket
    Then product should be added to basket successfully