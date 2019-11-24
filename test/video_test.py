import pytest
from hashlib import sha3_256
from requests import Session, get

astley = 'https://ia801602.us.archive.org/11/items/Rick_Astley_Never_Gonna_Give_You_Up/Rick_Astley_Never_Gonna_Give_You_Up.mp4'
# Get video hash for easy watch and delete
vid_hash = sha3_256(get(astley).content).hexdigest()

# Use unauthenticated session to make sure access control works
o = Session()
# Use a session with pytest user to upload
s = Session()

# Log in first
s.post('http://localhost/login', data={'username':'pytest', 'password':'testpassword'})

# Unauthed can't upload
def test_upload():
    assert not o.post('http://localhost/video/upload', data={'userid':'1', 'title':'Astley', 'description':'haha goteem', 'link':astley}).ok

# Authed can upload
def test_upload_unauth():
    assert s.post('http://localhost/video/upload', data={'userid':'1', 'title':'Astley', 'description':'haha goteem', 'link':astley}).ok

# Unauthed can watch
def test_watch():
    assert s.get(f'http://localhost/video/watch?hash={vid_hash}').ok

# Authed can watch
def test_watch():
    assert o.get(f'http://localhost/video/watch?hash={vid_hash}').ok

# Unauthed can't delete
def test_delete():
    assert not o.post('http://localhost/video/delete', data={'hash':vid_hash}).ok

# Authed can delete
def test_delete():
    assert s.post('http://localhost/video/delete', data={'hash':vid_hash}).ok

# Logout
s.get('http://localhost/video/logout')

