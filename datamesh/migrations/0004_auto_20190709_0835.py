# Generated by Django 2.2.2 on 2019-07-09 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamesh', '0003_auto_20190703_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logicmodulemodel',
            name='endpoint',
            field=models.CharField(help_text="Endpoint of the model with leading and trailing slashs, p.e.: '/siteprofiles/'", max_length=255),
        ),
    ]
