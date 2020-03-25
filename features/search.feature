Feature: Login
  Check user can login with valid username and password

  Scenario Outline: Search test
    Given I open search page
    When I type "<searchstring>" in search field
    When I click search button
    Then I see element with text "<resulttext>"

    Examples:
      | searchstring | resulttext                                       |
      | TrumpKlon    | Donald Trump personality simulator in the world. |
