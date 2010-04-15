from __future__ import absolute_import

from . import base

class Profile(base.Resource):
    """
    An encoding profile (size, compression options, etc.)
    """
    def __repr__(self):
        return "<Profile: %s>" % self.name
        
class ProfileManager(base.Manager):
    resource_class = Profile
    
    def all(self, page=1):
        """
        Get a list of all encoding profiles. Paginated.

        :param page: Page number
        :rtype: list of :class:`Profile` instances.
        """
        return self._list('/encoding_profiles', 'encoding_profiles')
        
    def get(self, id):
        """
        Look up an encoding profile by ID.

        :param id: The profile ID
        :rtype: A :class:`Profile` instance.
        """
        return self._get('/encoding_profiles/%s' % id, 'encoding_profile')