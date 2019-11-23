import pytest
import requests

def login(data):
    try:
        r = requests.post("https://localhost/login", data=data, verify=False)
    except Exception as e:
        print(e)
        return None
    return r.status_code


def main():
    data = {"username": "pytest", "password":"testpassword"}
    y = login(data)
    if y!= 200:
        print("unsuccessful login with correct creds")
    else:
        print("Successful Login with correct creds")

    data = {"username": "pytest", "password":"badpass"}

    y = login(data)
    if y!= 200:
        print("unsuccessful login with bad password")
    else:
        print("Successful Login with bad password")

    
    data = {"username": "badusername", "password":"badpass"}

    y = login(data)
    if y!= 200:
        print("unsuccessful login with bad everything")
    else:
        print("Successful Login with bad everything")
