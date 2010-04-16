from __future__ import absolute_import

from . import base
import urllib

class Job(base.Resource):
    """
    An encoding task.
    """
    def __repr__(self):
        return "<Job: %s - %s>" % (self.id, self.current_status)
    
    # HDCloud uses the key "complete?" which isn't valid Python, so alias it.
    @property
    def complete(self):
        return self._info['complete?']
    
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
        
    def create(self, source, destination, files, profiles, priority=5,
               use_file_cache=True, remote_id=None, callback_url=None):
        """
        Kick off a new encoding task

        :param source: The :class:`Store` containing the source file.
        :param destination: The :class:`Store` to store the output file(s)
        :param files: A list of filenames in the source store to encode.
        :param profiles: A list of :class:`Profile` for encoding.
        :param priority: Integer, 1-10; higher numbers are higher priorities.
        :param use_file_cache: Cache the source file in HD Cloud's cache?
        :param remote_id: An arbitrary string identifying the job.
        :param callback_url: A webhook that will get POSTed to when the job completes.
        :rtype: a list of :class:`Job` instances that have been kicked off.
        """
        params = [
            ('job[source_id]',      int(getattr(source, 'id', source))),
            ('job[destination_id]', int(getattr(source, 'id', source))),
            ('job[priority]',       int(priority)),
            ('job[use_file_cache]', use_file_cache and 'true' or 'false'),
        ]

        params.extend([('files[]', f) for f in files])

        prof_ids = [int(getattr(p, 'id', p)) for p in profiles]
        params.extend([('encoding_profile_ids[]', p) for p in prof_ids])

        if remote_id:
            params.append(('job[remote_id]', remote_id))
        if callback_url:
            params.append(('job[callback_url]', callback_url))
        
        resp, body = self.api.client.post('/jobs', body=urllib.urlencode(params))
        return [self.resource_class(self, j['job']) for j in body]
        
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
        