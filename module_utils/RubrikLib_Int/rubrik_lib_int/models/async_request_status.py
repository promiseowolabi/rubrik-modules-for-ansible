# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AsyncRequestStatus(Model):
    """AsyncRequestStatus.

    :param id: The ID of the request object. Use it to poll the status.
    :type id: str
    :param status: Status of the id.
    :type status: str
    :param progress: The current progress in terms of percentage of the async
     request.
    :type progress: float
    :param start_time: The start time of the request
    :type start_time: datetime
    :param end_time: The end time of the request
    :type end_time: datetime
    :param error: Any errors encountered
    :type error: :class:`RequestErrorInfo
     <rubriklib_int.models.RequestErrorInfo>`
    :param links: References to any related objects
    :type links: list of :class:`Link <rubriklib_int.models.Link>`
    """

    _validation = {
        'id': {'required': True},
        'status': {'required': True},
        'links': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'progress': {'key': 'progress', 'type': 'float'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'error': {'key': 'error', 'type': 'RequestErrorInfo'},
        'links': {'key': 'links', 'type': '[Link]'},
    }

    def __init__(self, id, status, links, progress=None, start_time=None, end_time=None, error=None):
        self.id = id
        self.status = status
        self.progress = progress
        self.start_time = start_time
        self.end_time = end_time
        self.error = error
        self.links = links