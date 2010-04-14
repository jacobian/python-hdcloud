from __future__ import absolute_import

from hdcloud import Profile
from .fakeserver import FakeHDCloud
from .utils import assert_isinstance

hdcloud = FakeHDCloud()

def test_all_profiles():
    ps = hdcloud.profiles.all()
    hdcloud.assert_called('GET', '/encoding_profiles.json')
    [assert_isinstance(p, Profile) for p in ps]
    
def test_get_store():
    p = hdcloud.profiles.get(id=1)
    hdcloud.assert_called('GET', '/encoding_profiles/1.json')
    assert p.name == 'Example Profile'