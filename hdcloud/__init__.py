from __future__ import absolute_import

__version__ = '1.0'

from .client import HDCloudClient
from .jobs import Job, JobManager
from .stores import Store, StoreManager
from .profiles import Profile, ProfileManager

class HDCloud(object):
    """
    Access to the HDCloud API.
    
    To use, first create an instance with your creds::
    
        >>> hdcloud = HDCloud(USERNAME, PASSWORD)
        
    Then call methods::
        
        >>> hdcloud.jobs.all()
        [...]
        
        >>> hdcloud.jobs.get(id=1)
        [...]
        
    Methods are named as documented at http://hdcloud.com/api/v1/help.
    """
    
    def __init__(self, username, password):
        self.client = HDCloudClient(username, password)
        self.jobs = JobManager(self)
        self.stores = StoreManager(self)
        self.profiles = ProfileManager(self)