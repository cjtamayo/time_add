Feature: Adding the time

  Scenario: No time is entered
    Given a working time add function
      When no time is entered
      Then a time of 0:00 is returned
