from __future__ import absolute_import

from . import base

class Store(base.Resource):
    def __repr__(self):
        return "<Store: %s>" % self.name
        
class StoreManager(base.Manager):
    resource_class = Store
    
    def all(self):
        return self._list('/stores', 'stores')
        
    def get(self, id):
        return self._get('/stores/%s' % id, 'store')