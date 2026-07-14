**Title**
Automated Testing of the Web Application
https://opensource-demo.orangehrmlive.com

**Project Objective**
The objective of this project is to automate the testing of the web application
https://opensource-demo.orangehrmlive.com by
simulating user actions and validating core functionalities. The goal is to ensure key
modules like login, menu accessibility, user management, and logout are functioning as
intended.

**Scope**
The automation is designed to simulate real-world usage patterns such as form
interactions, menu navigation, and authentication validation. Tests will be executed
across multiple browsers to ensure cross-browser compatibility. The system will interact
with various web elements and execute test cases covering both positive and negative
scenarios.

**Preconditions**
A comprehensive test suite must be designed, including both valid (positive) and
invalid (negative) test scenarios.
Each test case execution must include logging of results.
Explicit waits should be used wherever applicable to ensure reliable synchronization
with UI events.


**Automation Approach**
This project implements the above objective using Selenium WebDriver with Python,
structured with the Page Object Model (POM) design pattern, and executed via
pytest.
