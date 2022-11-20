*** Settings ***
Resource  resource.robot
Test Setup  Input New Command


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  ville  ville123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Input New Command
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists
    
Register With Too Short Username And Valid Password
    Input Credentials  v  ville123
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  ville  v
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  ville  villeville
    Output Should Contain  Password cannot contain only letters


