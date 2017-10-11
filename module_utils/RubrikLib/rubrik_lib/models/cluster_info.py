# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ClusterInfo(Model):
    """ClusterInfo.

    :param id: ID of the Rubrik cluster
    :type id: str
    :param version: Rubrik cluster software version
    :type version: str
    :param api_version: REST API version
    :type api_version: str
    """

    _validation = {
        'id': {'required': True},
        'version': {'required': True},
        'api_version': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'api_version': {'key': 'apiVersion', 'type': 'str'},
    }

    def __init__(self, id, version, api_version):
        self.id = id
        self.version = version
        self.api_version = api_version