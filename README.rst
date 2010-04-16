Python bindings to the HD Cloud API
===================================

This is a cloud for the `HD Cloud API <http://hdcloud.com/api/v1/help/>`_.

You'll need an HD Cloud account to use this library. You can either use your
account's username/password, or you can use a developer token from your user
profile page and use those credentials instead.

Usage
-----

First create an instance with your creds::

    >>> from hdcloud import HDCloud
    >>> hdcloud = HDCloud(USERNAME, PASSWORD)
    
Then call methods::
    
    >>> hdcloud.jobs.all()
    [<Job: 12345 - completed>]
    
    >>> hdcloud.jobs.get(id=12345)
    <Job: 12345 - completed>
    
For details, `see the documentation
<http://packages.python.org/python-hdcloud/`_ and/or HD Cloud's `API
documentation <http://hdcloud.com/api/v1/help/>`_.

Contributing
------------

Development takes place `on GitHub
<http://github.com/jacobian/python-hdcloud>`_; please file bugs/pull requests
there.

Development on this project was funded by `Discovery <http://discovery.com/>_ -
thanks!