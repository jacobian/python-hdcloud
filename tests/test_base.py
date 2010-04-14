from __future__ import absolute_import

import hdcloud.base
from .fakeserver import FakeHDCloud
from hdcloud import Store
from hdcloud.base import Resource
from nose.tools import assert_equal, assert_not_equal, assert_raises

hdcloud = FakeHDCloud()

def test_resource_repr():
    r = Resource(None, dict(foo="bar", baz="spam"))
    assert_equal(repr(r), "<Resource baz=spam, foo=bar>")
        
def test_resource_lazy_getattr():
    s = Store(hdcloud.stores, {'id': 1})
    assert_equal(s.name, 'Example Store')
    hdcloud.assert_called('GET', '/stores/1.json')
    
    # Missing stuff still fails after a second get
    assert_raises(AttributeError, getattr, s, 'blahblah')
    hdcloud.assert_called('GET', '/stores/1.json')

def test_eq():
    # Two resources of the same type with the same id: equal
    r1 = Resource(None, {'id':1, 'name':'hi'})
    r2 = Resource(None, {'id':1, 'name':'hello'})
    assert_equal(r1, r2)

    # Two resoruces of different types: never equal
    r1 = Resource(None, {'id': 1})
    r2 = Store(None, {'id': 1})
    assert_not_equal(r1, r2)

    # Two resources with no ID: equal if their info is equal
    r1 = Resource(None, {'name': 'joe', 'age': 12})
    r2 = Resource(None, {'name': 'joe', 'age': 12})
    assert_equal(r1, r2)