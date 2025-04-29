@login
Feature: Test Login Functionality

  Background:
    Given user loads "login" page
    And the "login" page is loaded

  Scenario: Successful login with valid credentials
    When I fill "standard_user" into the "username_input" in "login" page
    And I fill "secret_sauce" into the "password_input" in "login" page
    And I click on the "login_button" in "login" page
    Then the "products" page is loaded

  Scenario Outline: Display error for invalid login credentials
    When I fill "<user_name>" into the "username_input" in "login" page
    And I fill "<password>" into the "password_input" in "login" page
    And I click on the "login_button" in "login" page
    Then user see "Epic sadface: Username and password do not match any user in this service" on the "login_error" in "login" page
    Examples:
      | user_name     | password     |
      | standard_user | secret_saue  |
      | standard_se   | secret_sauce |

  Scenario Outline: Display error for missing username or password
    When I fill "<text>" into the "<filed>" in "login" page
    And I click on the "login_button" in "login" page
    Then user see "<error_message>" on the "login_error" in "login" page
    Examples:
      | text          | filed          | error_message                      |
      | standard_user | username_input | Epic sadface: Password is required |
      | secret_sau    | password_input | Epic sadface: Username is required |

  Scenario: Display error when attempting login with empty username and password
    When I click on the "login_button" in "login" page
    Then user see "Epic sadface: Username is required" on the "login_error" in "login" page

  Scenario: Display locked out error for locked user attempting to login
    When I fill "locked_out_user" into the "username_input" in "login" page
    And I fill "secret_sauce" into the "password_input" in "login" page
    And I click on the "login_button" in "login" page
    Then user see "Epic sadface: Sorry, this user has been locked out." on the "login_error" in "login" page
