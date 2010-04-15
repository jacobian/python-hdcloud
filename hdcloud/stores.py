from __future__ import absolute_import

from . import base

class Store(base.Resource):
    """
    A storage location (FTP, S3, etc.) for videos.
    """
    def __repr__(self):
        return "<Store: %s>" % self.name
        
class StoreManager(base.Manager):
    resource_class = Store
    
    def all(self):
        """
        Get a list of all encoding stores. Paginated.

        :param page: Page number
        :rtype: list of :class:`Store` instances.
        """
        return self._list('/stores', 'stores')
        
    def get(self, id):
        """
        Look up a store by ID.

        :param id: The store ID.
        :rtype: A :class:`Store` instance.
        """
        return self._get('/stores/%s' % id, 'store')