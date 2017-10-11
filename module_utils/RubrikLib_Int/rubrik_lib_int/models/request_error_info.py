# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RequestErrorInfo(Model):
    """RequestErrorInfo.

    :param message: The error message for failed ids.
    :type message: str
    """

    _validation = {
        'message': {'required': True},
    }

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, message):
        self.message = message