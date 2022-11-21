*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  ville
    Set Register Password  ville123  ville123
    Submit Create
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  v
    Set Register Password  ville123  ville123
    Submit Create
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  ville
    Set Register Password  v  ville123
    Submit Create
    Register Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  ville
    Set Register Password  ville123  ville456
    Submit Create
    Register Should Fail With Message  Password and confirmation do not match

Login After Successful Registration
    Set Username  ville
    Set Register Password  ville123  ville123
    Submit Create
    Go To Login Page
    Set Username  ville
    Set Password  ville123
    Submit Credentials
    Login Should Succeed


Login After Failed Registration
    Set Username  nalle
    Set Register Password  ville123  ville456
    Submit Create
    Go To Login Page
    Set Username  nalle
    Set Password  ville123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Create
    Click Button  Register

Set Register Password
    [Arguments]  ${password}  ${confirmation}
    Input Password  password  ${password}
    Input Password  password_confirmation  ${confirmation}

