import pytest
from requests import post

def login(data):
    try:
        r = post("https://localhost/login", data=data, verify=False)
    except Exception as e:
        print(e)
        return None
    return r.ok

def goodlogin_test(data):
    assert login(data)

def badpass_test(data):
    assert login(data)

def baduser_test(data):
    assert login(data) 

def badeverything_test(data):
    assert login(data)


goodlogin_test({"username": "pytest", "password":"testpassword"})

badpass_test({"username": "pytest", "password":"badpass"})

baduser_test({"username": "badusername", "password":"testpassword"})

baseverything_test({"username": "badusername", "password":"badpass"})

