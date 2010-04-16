Jobs
====

.. currentmodule:: hdcloud

Jobs represent encoding tasks (current and completed).

.. autoclass:: JobManager
   :members: all, current, completed, failed, get, create, frames, delete, destroy_bulk
   
.. autoclass:: Job
   :members: frames, delete
   
   .. attribute:: bitrate
   .. attribute:: complete
   .. attribute:: current_progress
   .. attribute:: current_status
   .. attribute:: current_step
   .. attribute:: encoded_filename
   .. attribute:: encoding_profile_id
   .. attribute:: id
   .. attribute:: remote_id
   .. attribute:: resolution
   .. attribute:: source_filename
   .. attribute:: status_url