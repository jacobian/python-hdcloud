from __future__ import absolute_import

from . import base

class Store(base.Resource):
    def __repr__(self):
        return "<Store: %s>" % self.name
        
class StoreManager(base.Manager):
    resource_class = Store
    
    def list(self):
        return self._list('/stores', 'stores')