*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  testaaja
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ab
    Set Password  validpass123
    Set Password Confirmation  validpass123
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Invalid Password
    Set Username  testaaja
    Set Password  onlyletters
    Set Password Confirmation  onlyletters
    Submit Credentials
    Register Should Fail With Message  Password cannot consist only of letters

Register With Nonmatching Password And Password Confirmation
    Set Username  testaaja
    Set Password  first123
    Set Password Confirmation  second123
    Submit Credentials
    Register Should Fail With Message  Passwords don't match

Login After Succesful Registration
    Set Username  testaaja
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  testaaja
    Set Password  testi123
    Click Button  Login
    Login Should Succeed

Login After Failed Registration
    Set Username  testaaja
    Set Password  first123
    Set Password Confirmation  second123
    Submit Credentials
    Register Should Fail With Message  Passwords don't match
    Click Link  Login
    Set Username  testaaja
    Set Password  first123
    Click Button  Login
    Login SHould Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open


Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}
