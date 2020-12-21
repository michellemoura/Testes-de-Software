Feature: LEAD Platform

   @login
Scenario: Effect login (1a)
  Given that the user is on the login page
  When the user provides a login with valid data
  Then the system directs the user to the home page

  @highContrast
Scenario: Enable system contrast mode (2a)
  Given that the user is logged in to the system
  When the user clicks the Enable high contrast option in the accessibility bar
  Then the system updates with high contrast colors


  @myCourses
Scenario: Go to the module my courses (3a)
Given that the user is logged in to the system2
When  user click on my courses module
Then the system presents the course content screen

  @openSelections
Scenario: go to open selections module (4a)
Given that the user is logged in to the system3
When the user clicks on the open selections module
Then the system shows open selections

