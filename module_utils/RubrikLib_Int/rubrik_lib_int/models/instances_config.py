# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class InstancesConfig(Model):
    """InstancesConfig.

    :param job_id: job id of the job
    :type job_id: str
    :param status: Status of the job
    :type status: str
    """

    _validation = {
        'job_id': {'required': True},
    }

    _attribute_map = {
        'job_id': {'key': 'jobId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(self, job_id, status=None):
        self.job_id = job_id
        self.status = status