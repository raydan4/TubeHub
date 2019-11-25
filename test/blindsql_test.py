import pytest
from requests import post, Session, get

s = Session()

def test_valid_search():
    assert s.post('http://localhost/search/results', data={'Search':'test'}).ok

def test_valid_sql_injection():
    assert s.post('http://localhost/search/results', data={'Search':'\' or 1=1'}).ok

def test_bad_sql_injection():
    assert not s.post('http://localhost/search/results', data={'Search':'\' or 1=1; select * from people'}).ok


