import httplib2
import urlparse
import urllib
import hdcloud
from . import exceptions
try:
    import json
except ImportError:
    import simplejson as json
    
class HDCloudClient(httplib2.Http):
    
    USER_AGENT = 'python-hdcloud/%s' % hdcloud.__version__
    BASE_URL = 'http://hdcloud.com/api/v1/'
    
    def __init__(self, username, password):
        super(HDCloudClient, self).__init__()
        self.add_credentials(username, password)
        self.force_exception_to_status_code = True
        
    def request(self, url, method, *args, **kwargs):
        url = urlparse.urljoin(self.BASE_URL, url.lstrip('/'))
        
        # Make sure to hardcode requests for JSON
        scheme, netloc, path, query, fragment = urlparse.urlsplit(url)
        path = "%s.json" % path
        url = urlparse.urlunsplit((scheme, netloc, path, query, fragment))
        
        # Add User-Agent headers
        kwargs.setdefault('headers', {})
        kwargs['headers']['User-Agent'] = self.USER_AGENT
        
        resp, body = self._hdc_request(url, method, *args, **kwargs)
        
        if resp.status in (400, 401, 403, 404, 406, 413, 500):
            raise exceptions.from_response(resp, body)
            
        return resp, body
    
    def _hdc_request(self, url, method, *args, **kwargs):
        # Separate method for mocking and testing.
        resp, body = super(HDCloudClient, self).request(url, method, *args, **kwargs)
        body = json.loads(body) if body else None
        return resp, body
    
    def get(self, url, **kwargs):
        return self.request(url, 'GET', **kwargs)
    
    def post(self, url, **kwargs):
        return self.request(url, 'POST', **kwargs)
    
    def put(self, url, **kwargs):
        return self.request(url, 'PUT', **kwargs)
    
    def delete(self, url, **kwargs):
        return self.request(url, 'DELETE', **kwargs)
    
