"""
A fake server that "responds" to methods with pre-canned results.

All the results come from the docs (http://hdcloud.com/api/v1/help). Places
where the actual API differs from the docs will be noted.
"""

from __future__ import with_statement
from __future__ import absolute_import

import httplib2
from hdcloud import HDCloud
from hdcloud.client import HDCloudClient
from nose.tools import assert_equal
from .utils import fail, assert_in, assert_not_in, assert_has_keys

class FakeHDCloud(HDCloud):
    def __init__(self, username=None, password=None):
        super(FakeHDCloud, self).__init__('username', 'password')
        self.client = FakeClient()

    def assert_called(self, method, url, body=None):
        """
        Assert than an API method was just called.
        """
        expected = (method, url)
        called = self.client.callstack[-1][0:2]

        assert self.client.callstack, "Expected %s %s but no calls were made." % expected
        
        assert expected == called, 'Expected %s %s; got %s %s' % (expected + called)
        
        if body is not None:
            assert_equal(self.client.callstack[-1][2], body)
        
        self.client.callstack = []
        
class FakeClient(HDCloudClient):
    def __init__(self):
        self.username = 'username'
        self.password = 'password'
        self.callstack = []
        
    def _request(self, url, method, *args, **kwargs):
        # Check that certain things are called correctly
        if method in ['GET', 'DELETE']:
            assert_not_in('body', kwargs)
        elif method in ['PUT', 'POST']:
            assert_in('body', kwargs)
        
        # Check ?format=json
        assert_in('format=json', url)
        
        # Call a method on self instead
        munged_url = url.replace(self.BASE_URL, '/').split('?', 1)[0]
        callback = "%s_%s" % (method.lower(), munged_url.strip('/').replace('/', '_'))
        if not hasattr(self, callback):
            fail('Called unknown API method: %s %s' % (method, url))
        
        # Note the call
        self.callstack.append((method, munged_url, kwargs.get('body', None)))
        
        status, body = getattr(self, callback)(**kwargs)
        return httplib2.Response({"status": status}), body
        
    def get_encoding_profiles(self, **kw):
        return (200, {"encoding_profiles": [{"id": 1,
                       "encoded_filename_format_string": "%f_%p_%b_%wx%h.%e",
                       "name": "Example Profile",
                       "resolutions": [["400x300"]],
                       "audiobitrate": 96,
                       "brightcove_publisher_id": None,
                       "updated_at": None,
                       "framerate": 30.0,
                       "brightcove": False,
                       "output_ext": None,
                       "output_format": None,
                       "keyframe_interval": None,
                       "audio_sample_rate": 44100,
                       "bitrate_tolerance": None,
                       "letterbox": True,
                       "time_offset": None,
                       "bitrate": [500, 400, 300],
                       "description": "Example Profile",
                       "thumbnail_interval": None,
                       "thumbnail_offset": None,
                       "max_file_size": None,
                       "created_at": None,
                       "time_duration": None}]})
    
    def get_encoding_profile_1(self, **kw):
        return (200, {"encoding_profile": self.get_encoding_profiles(**kw)[0]})
    
    def get_jobs(self, **kw):
        return (200, [{"job": {"current_step": "encoding",
                               "source_filename": "beer-drinking-pig.mpg",
                               "encoding_profile_id": None,
                               "resolution": None,
                               "status_url": "http://example.com/api/v1/jobs/1.json",
                               "id": 1,
                               "current_status": "Encoding: Pass 1",
                               "bitrate": None,
                               "current_progress": 42,
                               "remote_id": "my-own-remote-id"}}])
    
    def get_jobs_1(self, **kw):
        return (200, self.get_jobs(**kw)[1][0])
    
    def get_jobs_1_frames(self, **kw):
        raise NotImplementedError
    
    def delete_jobs_1(self, **kw):
        return (200, None)
        
    def delete_jobs_destroy_bulk(self, **kw):
        return (200, None)
    
    def get_jobs_current(self, **kw):
        return (200, [{"job": {"current_step": "encoding",
                               "source_filename": "beer-drinking-pig.mpg",
                               "encoding_profile_id": None,
                               "resolution": None,
                               "status_url": "http://example.com/api/v1/jobs/1.json",
                               "id": 1,
                               "current_status": "Encoding: Pass 1",
                               "bitrate": None,
                               "current_progress": 42,
                               "remote_id": "my-own-remote-id"}}])

    def get_jobs_completed(self, **kw):
        return (200, [{"job": {"current_step": None,
                               "source_filename": "beer-drinking-pig.mpg",
                               "encoding_profile_id": None,
                               "resolution": None,
                               "status_url": "http://example.com/api/v1/jobs/1.json",
                               "id": 1,
                               "current_status": "completed",
                               "bitrate": None,
                               "encoded_filename": "beer-drinking-pig_1_800_1920x1080.mp4",
                               "complete?": True,
                               "current_progress": None,
                               "remote_id": "my-own-remote-id"}}])
    
    def get_jobs_failed(self, **kw):
        return (200, [{"job": {"current_step": "failed",
                               "source_filename": "beer-drinking-pig.mpg",
                               "encoding_profile_id": None,
                               "resolution": None,
                               "status_url": "http://example.com/api/v1/jobs/1.json",
                               "failed?": True,
                               "id": 1,
                               "current_status": "failed",
                               "bitrate": None,
                               "failure_code": 500,
                               "failure_message": "An unexpected application error occurred. Please contact support.",
                               "current_progress": None,
                               "remote_id": "my-own-remote-id"}}])
    
    def post_jobs(self, body, **kw):
        assert_has_keys(body, 
                        required = ['job[source_id]', 'job[destination_id]',
                                    'files[]', 'encoding_profile_ids[]'],
                        optional = ['job[priority]', 'job[use_file_cache]',
                                    'job[name]', 'job[callback_url]',
                                    'job[remote_id]'])
        return (200, self.get_jobs())
    
    def get_stores(self, **kw):
        return (200, {"stores": [{"id": 1,
                                  "name": "Example Store",
                                  "cdn": "S3",
                                  "username": "123abc",
                                  "auth_token": None,
                                  "description": "Example Store",
                                  "deleted": False,
                                  "host": None,
                                  "ref": "example-bucket",
                                  "user_id": 1,
                                  "authorized": False,
                                  "password": "cba321"}]})
                                  
    def get_stores_1(self, **kw):
        return (200, {"store": self.get_stores(**kw)[1]["stores"][0]})