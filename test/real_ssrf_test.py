import pytest
from requests import post


def test_sql_injection():
    r = post('http://localhost/return-files', data={'filename':'shadow', 'path':'/etc'})
    assert 'root:!::0:::::' in r.text

