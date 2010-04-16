Stores
======

.. currentmodule:: hdcloud

Stores represent a storage location (FTP, S3, etc.) for videos. They can't be
created through the API; you'll need to create them via the web console.

.. autoclass:: StoreManager
   :members: all, get

.. autoclass:: Store

    The documentation doesn't explain what all the attributes mean,
    but the names are relatively self-explanatory, I hope:
   
    .. attribute:: authorized
    .. attribute:: auth_token
    .. attribute:: deleted
    .. attribute:: description
    .. attribute:: host
    .. attribute:: id
    .. attribute:: name
    .. attribute:: password
    .. attribute:: ref
    .. attribute:: username
    .. attribute:: user_id
