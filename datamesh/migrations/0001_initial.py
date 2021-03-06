# Generated by Django 2.2.2 on 2019-06-13 14:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workflow', '0014_rename_org_uuid'),
        ('gateway', '0003_auto_20190415_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogicModuleModel',
            fields=[
                ('logic_module_model_uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=128)),
                ('endpoint', models.CharField(blank=True, help_text='Endpoint of the model', max_length=255)),
                ('logic_module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='gateway.LogicModule')),
            ],
            options={
                'unique_together': {('logic_module', 'model')},
            },
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('relationship_uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('origin_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joins_origins', to='datamesh.LogicModuleModel')),
                ('related_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joins_relateds', to='datamesh.LogicModuleModel')),
            ],
            options={
                'unique_together': {('relationship_uuid', 'origin_model', 'related_model')},
            },
        ),
        migrations.CreateModel(
            name='JoinRecord',
            fields=[
                ('join_records_uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('record_id', models.PositiveIntegerField(blank=True, null=True)),
                ('record_uuid', models.UUIDField(blank=True, null=True)),
                ('related_record_id', models.PositiveIntegerField(blank=True, null=True)),
                ('related_record_uuid', models.UUIDField(blank=True, null=True)),
                ('organization', models.ForeignKey(blank=True, help_text='Related Organization with access', null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.Organization')),
                ('relationship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joinrecords', to='datamesh.Relationship')),
            ],
        ),
        migrations.AddConstraint(
            model_name='joinrecord',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('record_id', None), ('record_uuid', None), _negated=True), models.Q(models.Q(('record_id', None), models.Q(_negated=True, record_uuid=None)), models.Q(models.Q(_negated=True, record_id=None), ('record_uuid', None)), _connector='OR')), name='one_record_primary_key'),
        ),
        migrations.AddConstraint(
            model_name='joinrecord',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('related_record_id', None), ('related_record_uuid', None), _negated=True), models.Q(models.Q(('related_record_id', None), models.Q(_negated=True, related_record_uuid=None)), models.Q(models.Q(_negated=True, related_record_id=None), ('related_record_uuid', None)), _connector='OR')), name='one_related_record_primary_key'),
        ),
        migrations.AlterUniqueTogether(
            name='joinrecord',
            unique_together={('relationship', 'record_id', 'record_uuid', 'related_record_id', 'related_record_uuid', 'organization')},
        ),
    ]
