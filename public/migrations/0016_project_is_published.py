# Generated by Django 2.0.7 on 2018-08-10 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0015_projectimage_image_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
