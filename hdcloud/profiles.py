from __future__ import absolute_import

from . import base

class Profile(base.Resource):
    def __repr__(self):
        return "<Profile: %s>" % self.name
        
class ProfileManager(base.Manager):
    resource_class = Profile
    
    def list(self):
        return self._list('/profiles', 'encoding_profiles')