from typing import Any

from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response

from workflow.models import Organization

from seeds.admin import OrganizationAdmin
from workflow.permissions import IsSuperUser


@api_view(['POST'])
@permission_classes([IsSuperUser, ])
def seed(request: Request, *args: Any, **kwargs: Any) -> Response:
    organization, _ = Organization.objects.get_or_create(
        name='Robot Organization',
    )

    request.META['HTTP_REFERER'] = '/'  # (hack for now) - think of better solution:
    # p.e. adapt OrganizationAdmin.provide_seed

    response = OrganizationAdmin.provide_seed(
        request, organization_uuid=str(organization.organization_uuid), is_robot_test=True)
    # Todo: get messages from request

    return response

# ToDo: Write delete_seed method in OrganizationAdmin
