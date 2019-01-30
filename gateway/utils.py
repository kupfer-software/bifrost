import datetime
import re
import requests

from django.conf import settings

from rest_framework.settings import perform_import
from rest_framework.request import Request

from workflow import views as wfv
from workflow import models as wfm

from .models import LogicModule
from . import exceptions


SWAGGER_LOOKUP_FIELD = 'swagger'
SWAGGER_LOOKUP_FORMAT = 'json'
SWAGGER_LOOKUP_PATH = 'docs'
MODEL_VIEWSETS_DICT = {
    wfm.WorkflowTeam: wfv.WorkflowTeamViewSet,
    wfm.WorkflowLevel2: wfv.WorkflowLevel2ViewSet,
    wfm.WorkflowLevel1: wfv.WorkflowLevel1ViewSet,
    wfm.CoreUser: wfv.CoreUserViewSet,
    wfm.User: wfv.UserViewSet,
    wfm.Group: wfv.GroupViewSet,
    wfm.Organization: wfv.OrganizationViewSet,
    wfm.Milestone: wfv.MilestoneViewSet,
    wfm.WorkflowLevel2Sort: wfv.WorkflowLevel2SortViewSet,
}


def get_swagger_urls(service: str = None) -> dict:
    """
    Get the endpoint of the service in the database and append
    with the OpenAPI path

    :param str service: the name of the service
    :return: dict
             Key-value pair with service name and OpenAPI schema URL of it
    """
    if service is None:
        modules = LogicModule.objects.values(
            'name', 'endpoint').all()
    else:
        modules = LogicModule.objects.values(
            'name', 'endpoint').filter(name__istartswith=service)

    if len(modules) == 0 and service is not None:
        msg = 'Service "{}" not found.'.format(service)
        raise exceptions.ServiceDoesNotExist(msg, 404)

    module_urls = dict()
    for module in modules:
        swagger_url = '{}/{}/{}.{}'.format(
            module['endpoint'], SWAGGER_LOOKUP_PATH,
            SWAGGER_LOOKUP_FIELD, SWAGGER_LOOKUP_FORMAT
        )
        module_name = re.sub('_service$', '', module['name'].lower())
        module_urls[module_name] = swagger_url

    return module_urls


def get_swagger_from_url(api_url: str):
    """
    Get the swagger file of the service at the given url

    :param api_url:
    :return: dictionary representing the swagger definition
    """
    try:
        return requests.get(api_url).json()
    except requests.exceptions.ConnectionError as error:
        raise requests.exceptions.ConnectionError(
            f'Please, check that {api_url} is accessible.') from error


def datetime_handler(obj):
    """
    JSON doesn't have a default datetime type, so this is why Python can't
    handle it automatically. So you need to make the datetime into a string.
    """
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()


def validate_bifrost_object_access(request: Request, obj, action):
    """
    Raise a PermissionDenied-Exception in case the User has no access to
    the object or return None.
    :param obj:
    :return None:
    """
    model = obj._meta.model
    # instantiate ViewSet with action for has_obj_permission
    viewset = MODEL_VIEWSETS_DICT[model](action=action)

    permissions = getattr(viewset, 'permission_classes',
                          # perform_import for default DRF_Permission_setting
                          perform_import(settings.REST_FRAMEWORK[
                               'DEFAULT_PERMISSION_CLASSES'],
                           'REST_FRAMEWORK.DEFAULT_PERMISSION_CLASSES'))
    for permission_class in permissions:
        if not permission_class().has_object_permission(request, viewset, obj):
            raise exceptions.PermissionDenied(
              f'You do not have access to this instance of {model.__name__}.')
    return None
