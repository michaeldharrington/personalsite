# Generated by Django 2.0.7 on 2018-08-08 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0012_remove_project_objective'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimage',
            name='bg_color',
            field=models.CharField(default='#f2f2f2', max_length=6),
        ),
    ]
