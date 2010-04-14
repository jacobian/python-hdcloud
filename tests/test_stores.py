from __future__ import absolute_import

from hdcloud import Store
from .fakeserver import FakeHDCloud
from .utils import assert_isinstance

hdcloud = FakeHDCloud()

def test_all_stores():
    stores = hdcloud.stores.all()
    hdcloud.assert_called('GET', '/stores.json')
    [assert_isinstance(s, Store) for s in stores]
    
def test_get_store():
    store = hdcloud.stores.get(id=1)
    hdcloud.assert_called('GET', '/stores/1.json')
    assert store.name == 'Example Store'
    