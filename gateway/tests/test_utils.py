import factories

from django.test import TestCase
from rest_framework.test import APIRequestFactory

from gateway.exceptions import PermissionDenied
from gateway.utils import validate_bifrost_object_access


class UtilsValidateBifrostObjectAccessTest(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.core_user = factories.CoreUser()

    def test_validate_bifrost_wfl1_access_superuser(self):
        request = self.factory.get('/workflowlevel1/')
        self.core_user.is_superuser = True
        self.core_user.save()
        request.user = self.core_user.user
        wflvl1 = factories.WorkflowTeam()
        ret = validate_bifrost_object_access(request, wflvl1, 'retrieve')
        self.assertEqual(ret, None)

    def test_validate_bifrost_wfl1_not_authenticated_user(self):
        request = self.factory.get('/workflowlevel1/')
        self.core_user.is_superuser = True
        self.core_user.save()
        request.user = self.is_authenticated = False
        wflvl1 = factories.WorkflowTeam()
        expected_message = 'You do not have access to this instance of ' \
                           'WorkflowTeam.'
        with self.assertRaisesMessage(PermissionDenied, expected_message):
            validate_bifrost_object_access(request, wflvl1, 'retrieve')
