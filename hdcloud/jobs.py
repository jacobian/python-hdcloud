from __future__ import absolute_import

from . import base

class Job(base.Resource):
    def __repr__(self):
        return "<Job %s>" % self.id
        
class JobManager(base.Manager):
    resource_class = Job
    
    def all(self):
        return self._list('/jobs', 'jobs')