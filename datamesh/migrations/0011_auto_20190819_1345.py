# Generated by Django 2.2.3 on 2019-08-19 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamesh', '0010_auto_20190812_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logicmodulemodel',
            name='logic_module_endpoint_name',
            field=models.CharField(help_text="Without leading and trailing slashes, on local models enter the name of the app, p.e. 'workflow'.", max_length=255),
        ),
    ]
