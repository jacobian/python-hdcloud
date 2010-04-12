class HDCloudException(Exception):
    """
    The base exception class for all exceptions this library raises.
    """
    def __init__(self, code, message=None, details=None):
        self.code = code
        self.message = message or self.__class__.message
        self.details = details
        
    def __str__(self):
        return "%s (HTTP %s)" % (self.message, self.code)

_code_map = dict((c.http_status, c) for c in HDCloudException.__subclasses__())

def from_response(response, body):
    """
    Return an instance of a HDCloudException or subclass
    based on an httplib2 response. 
    
    Usage::
    
        resp, body = http.request(...)
        if resp.status != 200:
            raise exception_from_response(resp, body)
    """
    cls = _code_map.get(response.status, HDCloudException)
    if body:
        return cls(code=response.status, message=body['errors'][0]['message'])
    else:
        return cls(code=response.status)