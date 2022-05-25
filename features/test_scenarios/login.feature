Feature: Login feature

    Background: Preconditions
        Given I am on the login page
        When I validate elements are displayed

    Scenario: Validate login
        When I login with "angular" and "password" credentials
        Then I validate I am on the home page
        And I logout

    Scenario Outline: Validate login with wrong credentials and minimun length of username and password
        When I login with "<username>" and "<password>" credentials
        Then I can see a message saying "<message>"

        Examples:
            | username | password  | message                                                 |
            | angular  | password1 | Username or password is incorrect                       |
            | angular1 | password  | Username or password is incorrect                       |
            | an       | password  | Your username must be between 3 and 50 characters long  |
            | angular  | pa        | Your username must be between 3 and 100 characters long |
