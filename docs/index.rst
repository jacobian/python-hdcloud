Python bindings to the HDCloud API
==================================

.. module:: hdcloud
   :synopsys: A client for the HD Cloud API.
   
.. currentmodule:: hdcloud

Usage
-----

First create an instance with your creds::

    >>> from hdcloud import HDCloud
    >>> hdcloud = HDCloud(USERNAME, PASSWORD)

You'll need an HD Cloud account to use this library. You can either use your
account's username/password, or you can use a developer token from your user
profile page and use those credentials instead.

Then call methods on the :class:`HDCloud` object:

.. class:: HDCloud

    .. attribute:: jobs
    
        The :class:`JobManager` - start, stop, and query jobs.
        
    .. attribute:: profiles
    
        The :class:`ProfileManager` - query encoding profiles.
        
    .. attribute:: stores
    
        The :class:`StoreManager` - query file storage locations.
        
For example::

    >>> hdcloud.jobs.all()
    [<Job: 12345 - completed>]
    
    >>> hdcloud.stores.get(id=2)
    <Store: my store>

For details, see:

.. toctree::
   :maxdepth: 1
   
   jobs
   profiles
   stores

.. seealso::

    HD Cloud's `API documentation <http://hdcloud.com/api/v1/help/>`_.

Contributing
------------

Development takes place `on GitHub
<http://github.com/jacobian/python-hdcloud>`_; please file bugs/pull requests
there. Run tests with ``python setup.py test``.

Development on this project was funded by `Discovery <http://discovery.com/>`_ -
thanks!