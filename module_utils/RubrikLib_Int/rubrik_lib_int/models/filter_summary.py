# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class FilterSummary(Model):
    """FilterSummary.

    :param date_config: Date range for the data.
    :type date_config: :class:`DateFilter <rubriklib_int.models.DateFilter>`
    :param task_status: Status of the task.
    :type task_status: list of str
    :param sla_domain: SLA domain IDs.
    :type sla_domain: list of str
    :param objects: Object IDs.
    :type objects: list of str
    :param object_type: Object types.
    :type object_type: list of str
    :param object_location: Object locations.
    :type object_location: list of str
    :param cluster_location: Cluster locations.
    :type cluster_location: list of str
    :param task_type: Task type.
    :type task_type: list of str
    :param compliance_status: Compliance status.
    :type compliance_status: list of str
    """

    _attribute_map = {
        'date_config': {'key': 'dateConfig', 'type': 'DateFilter'},
        'task_status': {'key': 'taskStatus', 'type': '[str]'},
        'sla_domain': {'key': 'slaDomain', 'type': '[str]'},
        'objects': {'key': 'objects', 'type': '[str]'},
        'object_type': {'key': 'objectType', 'type': '[str]'},
        'object_location': {'key': 'objectLocation', 'type': '[str]'},
        'cluster_location': {'key': 'clusterLocation', 'type': '[str]'},
        'task_type': {'key': 'taskType', 'type': '[str]'},
        'compliance_status': {'key': 'complianceStatus', 'type': '[str]'},
    }

    def __init__(self, date_config=None, task_status=None, sla_domain=None, objects=None, object_type=None, object_location=None, cluster_location=None, task_type=None, compliance_status=None):
        self.date_config = date_config
        self.task_status = task_status
        self.sla_domain = sla_domain
        self.objects = objects
        self.object_type = object_type
        self.object_location = object_location
        self.cluster_location = cluster_location
        self.task_type = task_type
        self.compliance_status = compliance_status