import pytest
from requests import post, Session, get

s = Session()
success = '<h1>[{&#39;title&#39;: &#39;Test&#39;}, {&#39;title&#39;: &#39;Random&#39;}]</h1>'

def test_sql_injection():
    assert success in s.post('http://localhost/search', data={'Search':'\' or 1=1'}).text

