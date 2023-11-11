*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  testaaja  testi123
    Output Should Contain  New user registered

Register With Already Taken Username and Valid Password
    Input Credentials  kalle  testi123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ab  validpass123
    Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  invalid123  validpass123
    Output Should Contain  Username must contain only lowercase letters

Register With Valid Username And Too Short Password
    Input Credentials  validuser  short
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  validuser  onlyletters
    Output Should Contain  Password cannot consist only of letters

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command
