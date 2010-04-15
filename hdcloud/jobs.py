from __future__ import absolute_import

from . import base
import urllib

class Job(base.Resource):
    """
    An encoding task.
    """
    def __repr__(self):
        return "<Job: %s>" % self.id
    
    def frames(self, page=1):
        """
        Get a list of captured frames from a job.
        
        :param page: Page number.
        :rtype: a list of filenames.
        """
        return self.manager.frames(self, page)
        
    def delete(self):
        """
        Delete (i.e. cancel) this job.
        """
        return self.manager.delete(self)
    
class JobManager(base.Manager):
    resource_class = Job
        
    def all(self, page=1):
        """
        Get a list of all jobs ever created. Paginated.

        :param page: Page number
        :rtype: list of :class:`Job` instances.
        """
        return self._list('/jobs?page=%s' % page)
        
    def current(self, page=1):
        """
        Get a list of currently running jobs. Paginated.

        :param page: Page number
        :rtype: list of :class:`Job` instances.
        """
        return self._list('/jobs/current?page=%s' % page)
        
    def completed(self, page=1):
        """
        Get a list of completed jobs. Paginated.

        :param page: Page number
        :rtype: list of :class:`Job` instances.
        """
        return self._list('/jobs/completed?page=%s' % page)
        
    def failed(self, page=1):
        """
        Get a list of all failed jobs. Paginated.

        :param page: Page number
        :rtype: list of :class:`Job` instances.
        """
        return self._list('/jobs/failed?page=%s' % page)
        
    def create(self, source, destination, files, encoding_profiles, priority=5,
               use_file_cache=True, name=None, callback_url=None):
        raise NotImplementedError
        
    def get(self, id):
        """
        Look up a job by ID.

        :param id: The job ID
        :rtype: A :class:`Job` instance.
        """
        return self._get('/jobs/%s' % id, 'job')

    def frames(self, obj, page=1):
        """
        Get a list of captured frames from a job.

        :param page: Page number.
        :param obj: The :class:`Job`, or its ID.
        :rtype: a list of filenames.
        """
        id = int(getattr(obj, 'id', obj))
        resp, body = self.api.client.get('/jobs/%s/frames?page=%s' % (id, page))
        return body['frames']['filenames']
        
    def delete(self, obj):
        """
        Delete (i.e. cancel) a job.
        """
        id = int(getattr(obj, 'id', obj))
        return self._delete('/jobs/%s' % id)
        
    def destroy_bulk(self, objs):
        """
        Delete (i.e. cancel) a bunch of jobs.

        :param objs: List of :class:`Job` instances, or their IDs.
        """
        ids = [int(getattr(o, 'id', o)) for o in objs]
        args = urllib.urlencode([('job_ids[]', id) for id in ids])
        return self._delete('/jobs/destroy_bulk?%s' % args)
        
    def _list(self, url):
        # The Job API uses a different response format from the rest of the API - 
        # instead of `{'jobs': [{...}]}`, it's `[{'job': {...}}]`
        resp, body = self.api.client.get(url)
        return [self.resource_class(self, i['job']) for i in body]
        