import pytest
from requests import post, Session, get

s = Session()

def test_sql_injection():
    assert s.post('http://localhost/file_upload', data={'filename':'shadow', 'path':'/etc'}).ok

