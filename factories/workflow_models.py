from factory import DjangoModelFactory, LazyAttribute, SubFactory

from workflow.models import (
    CoreUser as CoreUserM,
    Organization as OrganizationM,
    WorkflowLevel1 as WorkflowLevel1M,
    WorkflowLevel2 as WorkflowLevel2M,
    WorkflowTeam as WorkflowTeamM,
)
from .django_models import User, Group


class Organization(DjangoModelFactory):
    class Meta:
        model = OrganizationM

    name = 'Humanitec GmbH'


class CoreUser(DjangoModelFactory):
    class Meta:
        model = CoreUserM
        django_get_or_create = ('user',)

    user = SubFactory(User)
    name = LazyAttribute(lambda o: o.user.first_name + " " + o.user.last_name)
    organization = SubFactory(Organization)


class WorkflowLevel1(DjangoModelFactory):
    class Meta:
        model = WorkflowLevel1M

    name = 'Health and Survival for Syrians in Affected Regions'


class WorkflowLevel2(DjangoModelFactory):
    class Meta:
        model = WorkflowLevel2M

    name = 'Help Syrians'
    workflowlevel1 = SubFactory(WorkflowLevel1)


class WorkflowTeam(DjangoModelFactory):
    class Meta:
        model = WorkflowTeamM

    workflow_user = SubFactory(CoreUser)
    workflowlevel1 = SubFactory(WorkflowLevel1)
    role = SubFactory(Group)
