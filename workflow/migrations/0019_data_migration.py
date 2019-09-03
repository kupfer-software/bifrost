import json
import os

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import migrations

"""
Prerequisites:
    - On the cluster, get ProjectExtensions into file `projectextensions.json`:
        gcloud container clusters get-credentials cluster-1 --zone europe-west1-b --project <project-name>
        kubectl exec -n kupfer-dev -it extensionservice-9d8594d4d-rlhvm bash -- -c "python manage.py dumpdata --format=json --indent=4 extensions.ProjectExtension" > projectextensions.json

    - Copy projectextensions.json from local to bifrost
        kubectl cp projectextensions.json <namespace>/<bifrost>:/code/projectextensions.json

"""  # noqa


def populate_project_ids(apps, schema_editor):
    """
    For every ProjectExtension the WorkflowLevel2 should get the project_id into the new `project_id`-field.
    """
    wfl2_model = apps.get_model('workflow', 'WorkflowLevel2')
    db_alias = schema_editor.connection.alias
    project_extension_json = os.path.join(settings.BASE_DIR, 'projectextensions.json')
    try:
        with open(project_extension_json) as f:
            project_extensions = json.load(f)
    except FileNotFoundError:
        print('\nprojectextensions.json not found - Skipping data migration.')
        return

    for project_extension in project_extensions:
        workflowlevel2_uuid = project_extension['fields']['workflowlevel2_uuid']
        try:
            wfl2 = wfl2_model.objects.using(db_alias).get(level2_uuid=workflowlevel2_uuid)
        except ObjectDoesNotExist:
            print(f'{workflowlevel2_uuid} not found - Skipping.')
            continue
        wfl2.project_id = project_extension['fields']['project_id']
        wfl2.save()
        print(f'{wfl2} updated with project_id: {wfl2.project_id}.')


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0018_auto_20190822_0855'),
    ]

    operations = [

        migrations.RunPython(populate_project_ids,
                             migrations.RunPython.noop),

    ]
