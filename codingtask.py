# Section 2 
# write a function to validate email format based on given rules 

# must contain @
# must conatin domain (e.g .com)
# no spaces allowed
# should handle null/empty input

# return 
# true for a valid email 
# false for invalid email.

def is_valid_email(email):
    # Handle null or empty input
    if email is None or email == "":
        return False
    # No spaces allowed
    if " " in email:
        return False
    # Must contain '@'
    if "@" not in email:
        return False
    # Split into local and domain parts
    parts = email.split("@")
    if len(parts) != 2:
        return False
    local, domain = parts
    # Ensure both parts exist
    if not local or not domain:
        return False
    # Domain must contain a dot (e.g., .com)
    if "." not in domain:
        return False
    # Domain should not start or end with a dot
    if domain.startswith(".") or domain.endswith("."):
        return False
    return True



Section 1 
API Testing 
endpoint: randomuser.me/api/

tasks 
1 write atleast 6 testcases for this api

2 include;
positive testcases 
negative testcases 
edge cases 

3 define;
expected status codes 
validation points


Feature: Random User API Testing

  Background:
    Given the API base URL is "https://randomuser.me/api/"

   Positive Test Cases


  Scenario: Get a single random user
    When I send a GET request to "/"
    Then the response status code should be 200
    And the response should contain a "results" array
    And the "results" array should contain exactly 1 user
    And each user should have "name", "email", and "login.uuid"
    And the response should contain an "info" object

  Scenario: Get multiple users
    When I send a GET request to "/?results=5"
    Then the response status code should be 200
    And the "results" array should contain exactly 5 users
    And each user should have consistent structure
    And the "info.results" should be 5

  Scenario: Filter users by gender
    When I send a GET request to "/?gender=female"
    Then the response status code should be 200
    And all users in "results" should have gender "female"

   Negative Test Cases


  Scenario: Invalid results parameter
    When I send a GET request to "/?results=-10"
    Then the response status code should be 200
    And the API should return a default number of users
    And the "results" array should not be empty
    And the response format should remain valid

  Scenario: Invalid gender parameter
    When I send a GET request to "/?gender=unknown"
    Then the response status code should be 200
    And the API should ignore the invalid filter
    And the response should contain valid user data
    And the response structure should be correct


  Edge Test Cases


  Scenario: Large number of requested users
    When I send a GET request to "/?results=5000"
    Then the response status code should be 200
    And the API should handle the request gracefully
    And the "results" array should be returned without errors

  Scenario: Default behavior with no parameters
    When I send a GET request to "/"
    Then the response status code should be 200
    And the API should return default results
    And the "results" array should contain exactly 1 user

  Scenario: Deterministic response using seed
    When I send a GET request to "/?seed=abc&results=2"
    And I send the same GET request again
    Then both responses should be identical
    And the same users should be returned in both responses




Section 3 
ui testing 
scenario
you are testing a login page with;
email field
password field 
login button

Tasks 
write 5 functional test cases 
write 3 negative test cases
identify at least 3 possible bugs

bonus describe how you would automate this with selenium 

Feature: Login Page Functionality

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter a valid email
    And I enter a valid password
    And I click the login button
    Then I should be redirected to the dashboard

  Scenario: Email field accepts valid email format
    Given I am on the login page
    When I enter "user@example.com" in the email field
    Then the email should be accepted

  Scenario: Password field masks input
    Given I am on the login page
    When I type a password
    Then the password should be hidden or masked

  Scenario: Login button is clickable when fields are filled
    Given I am on the login page
    When I enter valid email and password
    Then the login button should be enabled

  Scenario: Pressing Enter submits the form
    Given I am on the login page
    When I enter valid credentials
    And I press Enter
    Then the login request should be submitted



Feature: Login Page Negative Scenarios

  Scenario: Login with invalid email format
    Given I am on the login page
    When I enter "invalid-email"
    And I enter a valid password
    And I click login
    Then I should see an email validation error

  Scenario: Login with empty fields
    Given I am on the login page
    When I leave email and password empty
    And I click login
    Then I should see required field errors

  Scenario: Login with incorrect credentials
    Given I am on the login page
    When I enter a valid email
    And I enter an incorrect password
    And I click login
    Then I should see an authentication error message


Possible Bugs

Email field accepts invalid formats (e.g. "user@com" passes validation).

Password field is not masked (security/privacy issue).

Login button is enabled even when fields are empty.

No error message shown for invalid credentials (poor UX).

Pressing Enter does nothing (form not properly submitted).

Case sensitivity issues (e.g., email treated incorrectly).

Slow response or multiple submissions when button is clicked repeatedly.

Approach with selenium

Setup
Install Selenium
Launch browser (Chrome/Firefox)
Navigate to login page
Locate Elements
Email field → by id, name, or css selector
Password field
Login button
Perform Actions
Send input (sendKeys)
Click button
Submit form
Assertions
Check URL change (successful login)
Validate error messages


Section 4 Bug Report
When a user enters correct email and password clicking login does nothing
Task 
write a complete bug report 

Bug ID: LOGIN-001
Title: Login button does not trigger any action with valid credentials

Description
When a user enters a valid email and password and clicks the login button, no action occurs. The user is not logged in, no error message is displayed, and there is no indication that the request was processed.

Steps to Reproduce
Navigate to the login page
Enter a valid email (e.g test@gmail.com)
Enter a valid password
Click the Login button

Expected Result
User should be authenticated successfully
User should be redirected to the dashboard (or home page)
A session should be created

Actual Result
Clicking the login button does nothing
No redirection occurs
No error is displayed




Section 4: SIT Question

During SIT, you notice that transactions processed through the mobile app are correctly reflected in core banking system but daily reconciliation report shows mismatches 

How would you approach identifying the root causes?
What specific checks would you perform?

I’d avoid assuming the core banking system is “fully correct” just because it looks right—reconciliation issues often come from timing, transformation, or aggregation differences, not outright failures.

I would break the investigation into layers:

1. Trace a Sample Set of Transactions
Pick a few mismatched transactions from the reconciliation report and trace them:
Mobile app → API → core banking → reconciliation report
Compare values at each stage (amount, timestamp, status, transaction ID)
This helps pinpoint where the mismatch is introduced.

2. Validate Data Flow and Integration Points
Check whether:
Transactions are being sent reliably from the mobile app
Middleware or APIs are dropping, duplicating, or modifying data
Message queues are processing all events correctly

3. Compare Timing & Cut-off Logic
Reconciliation reports often depend on batch timing, which is a common source of issues:
Are there timezone inconsistencies between systems?
Are late or retried transactions handled properly?

4. Check Data Transformation Rules
Sometimes the issue isn’t missing data—it’s altered data:

Currency rounding differences
Formatting issues (e.g., decimal precision)
Mapping errors (e.g., transaction types or statuses)

5. Investigate Report Generation Logic
The reconciliation report itself might be flawed:
Check on sql queries.


Some common culprits in SIT environments:
Transactions processed after report cut-off but included in core system
Duplicate messages due to retry mechanisms
Report query bug (missing filters or joins)
Timezone mismatch between systems
Batch job failure or partial execution


