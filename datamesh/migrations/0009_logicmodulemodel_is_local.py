# Generated by Django 2.2.3 on 2019-07-23 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamesh', '0008_auto_20190717_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='logicmodulemodel',
            name='is_local',
            field=models.BooleanField(default=False, help_text='Local model is taken from BiFrost'),
        ),
    ]
