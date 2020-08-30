from nose.tools import *
from gothonweb.app import app

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 200)

    rv = web.get('/hello', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    assert_in(b"Fill Out This Form", rv.data)

    data = {'name': 'Andro', 'greet': 'Au revoir'}
    rv = web.post('/hello', follow_redirects=True, data=data)
    assert_in(b'Andro', rv.data)
    assert_in(b'Au revoir', rv.data)
    