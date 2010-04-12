from __future__ import absolute_import

from . import base
import urllib

class Job(base.Resource):
    def __repr__(self):
        return "<Job %s>" % self.id
    
    def frames(self):
        return self.manager.frames(self.id)
        
    def delete(self):
        return self.manager.delete(self.id)
    
class JobManager(base.Manager):
    resource_class = Job
    
    def all(self, page=1):
        return self._list('/jobs?page=%s' % page, 'jobs')
        
    def current(self, page=1):
        return self._list('/jobs/current?page=%s' % page, 'jobs')
        
    def completed(self, page=1):
        return self._list('/jobs/completed?page=%s' % page, 'jobs')
        
    def failed(self, page=1):
        return self._list('/jobs/failed?page=%s' % page, 'jobs')
        
    def create(self, source, destination, files, encoding_profiles, priority=5,
               use_file_cache=True, name=None, callback_url=None):
        raise NotImplementedError
        
    def get(self, id):
        return self._get('/jobs/%s' % id, 'job')


    def frames(self, id):
        return self._get('/jobs/%s/frames' % id, 'job')
        
    def delete(self, id):
        return self._delete('/jobs/%s' % id)
        
    def delete_in_bulk(self, ids):
        args = urllib.urlencode(('job_ids[]', id) for id in ids)
        return self._delete('/jobs/destroy_bulk?%s' % args)