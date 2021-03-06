# Generated by Django 2.2.3 on 2019-07-15 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamesh', '0004_auto_20190709_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='logicmodulemodel',
            name='logic_module_endpoint_name',
            field=models.CharField(default='', help_text='Without leading and trailing slashes', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='logicmodulemodel',
            unique_together={('logic_module_endpoint_name', 'model')},
        ),
    ]
