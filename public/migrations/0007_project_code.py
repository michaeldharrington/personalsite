# Generated by Django 2.0.7 on 2018-08-03 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0006_auto_20180803_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='code',
            field=models.TextField(blank=True, null=True),
        ),
    ]