from __future__ import absolute_import

from . import base

class Profile(base.Resource):
    def __repr__(self):
        return "<Profile: %s>" % self.name
        
class ProfileManager(base.Manager):
    resource_class = Profile
    
    def all(self, page=1):
        return self._list('/encoding_profiles', 'encoding_profiles')
        
    def get(self, id):
        return self._get('/encoding_profiles/%s' % id, 'encoding_profile')