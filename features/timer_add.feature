Feature: Adding the time

  Scenario: No time is entered
    Given a working time add function
      When no time is entered
      Then a time of 0:00 is returned

  Scenario: One time is entered
    Given a working time add function
      When one time length is entered
      Then that time is returned

  Scenario Outline: Multiple time lengths added
    Given a working time add function
      When a <timeset> is entered
      Then the correct <timetotal> is returned

    Examples: Time sets
    | timeset   | timetotal |
    | test1     | total1    |
    | test2     | total2    |
    | test3     | total3    |
    | test4     | total4    |
