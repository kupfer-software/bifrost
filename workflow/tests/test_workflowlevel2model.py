import pytest
from django.db import IntegrityError

import factories


@pytest.mark.django_db()
def test_set_project_id():
    workflowlevel2_1 = factories.WorkflowLevel2.create()
    workflowlevel2_1.set_default_project_id()
    workflowlevel2_2 = factories.WorkflowLevel2.create(
        workflowlevel1=workflowlevel2_1.workflowlevel1)
    workflowlevel2_2.set_default_project_id()
    assert workflowlevel2_1.project_id == 10001
    assert workflowlevel2_2.project_id == 10002


@pytest.mark.django_db()
def test_unique_project_id():
    workflowlevel2 = factories.WorkflowLevel2.create()
    workflowlevel2.set_default_project_id()
    with pytest.raises(IntegrityError):
        factories.WorkflowLevel2.create(
            workflowlevel1=workflowlevel2.workflowlevel1,
            project_id=10001
        )
