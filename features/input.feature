Feature: Time Input

  Scenario Outline: Input
    Given I have <thing> as input
    when I have an unempty time list
    then the response should be <response>

   Examples: Times
    | thing   | response |
