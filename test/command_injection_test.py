import pytest
from requests import post

def test_command_injection():
    r = post('http://localhost/admin', data={'command':'echo "Hackers welcome!"'})
    assert r.json().get('output') == 'Hackers welcome!\n'

