import pytest
from requests import post

def login(data):
    return post("http://localhost/login", data=data).ok

def test_goodlogin():
    assert login({"username": "pytest", "password":"testpassword"})

def test_badpass():
    assert not login({"username": "pytest", "password":"badpass"})

def test_baduser():
    assert not login({"username": "badusername", "password":"testpassword"}) 

def test_badeverything():
    assert not login({"username": "badusername", "password":"badpass"})

