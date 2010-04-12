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
        
        # Make sure to hardcode ?format=json
        parsed = urlparse.urlsplit(url)
        query = [i for i in urlparse.parse_qsl(parsed.query) if i[0] != 'format']
        query.append(('format', 'json'))
        query = urllib.urlencode(query)
        url = urlparse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, query, parsed.fragment))
        
        # Add User-Agent headers
        kwargs.setdefault('headers', {})
        kwargs['headers']['User-Agent'] = self.USER_AGENT
        
        resp, body = super(HDCloudClient, self).request(url, method, *args, **kwargs)
        body = json.loads(body) if body else None
        
        if resp.status in (400, 401, 403, 404, 406, 413, 500):
            raise exceptions.from_response(resp, body)
            
        return resp, body
    
    def get(self, url, **kwargs):
        return self.request(url, 'GET', **kwargs)
    
    def post(self, url, **kwargs):
        return self.request(url, 'POST', **kwargs)
    
    def put(self, url, **kwargs):
        return self.request(url, 'PUT', **kwargs)
    
    def delete(self, url, **kwargs):
        return self.request(url, 'DELETE', **kwargs)
    
