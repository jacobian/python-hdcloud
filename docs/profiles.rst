Encoding profiles
=================

.. currentmodule:: hdcloud

Encoding profiles store information about particular encoding options (size,
compression, format, etc.). They can't be created through the API; you'll need
to create them via the web console.

.. autoclass:: ProfileManager
   :members: all, get

.. autoclass:: Profile
   
    The documentation doesn't explain what all the attributes mean,
    but the names are relatively self-explanatory, I hope:
    
    .. attribute:: audiobitrate
    .. attribute:: audio_sample_rate
    .. attribute:: bitrate
    .. attribute:: bitrate_tolerance
    .. attribute:: brightcove
    .. attribute:: brightcove_publisher_id
    .. attribute:: created_at
    .. attribute:: description
    .. attribute:: encoded_filename_format_string
    .. attribute:: framerate
    .. attribute:: id
    .. attribute:: keyframe_interval
    .. attribute:: letterbox
    .. attribute:: max_file_size
    .. attribute:: name
    .. attribute:: output_ext
    .. attribute:: output_format
    .. attribute:: resolutions
    .. attribute:: thumbnail_interval
    .. attribute:: thumbnail_offset
    .. attribute:: time_duration
    .. attribute:: time_offset
    .. attribute:: updated_at
   