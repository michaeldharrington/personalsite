# Generated by Django 2.0.7 on 2018-08-03 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_auto_20180803_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='code',
            field=models.TextField(blank=True, null=True),
        ),
    ]