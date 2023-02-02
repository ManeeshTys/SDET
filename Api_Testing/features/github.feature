Feature: GitHub API Validation

    Scenario: session management check
        Given I have github credentials
        When I hit getRepo API gitHub
        Then staus code of response should be 200