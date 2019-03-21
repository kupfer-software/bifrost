# Generated by Django 2.0.7 on 2019-03-15 10:57

from django.db import migrations
from workflow.models import WorkflowLevel2


def forwards(apps, schema_editor):
    for wf2 in WorkflowLevel2.objects.all():
        user = wf2.created_by
        if user:
            wf2._created_by = user.core_user
        wf2.save()


def backwards(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0015_auto_20190315_1050'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards)
    ]