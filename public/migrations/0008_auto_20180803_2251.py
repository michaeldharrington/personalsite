# Generated by Django 2.0.7 on 2018-08-03 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0007_project_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='img',
            new_name='img_main',
        ),
        migrations.RemoveField(
            model_name='project',
            name='full_text',
        ),
        migrations.AddField(
            model_name='project',
            name='detail',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='left_text',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='objective',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='path',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='project',
            name='right_images',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='right_text',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='tile',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='created',
            field=models.DateField(default='date.today'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='highlighted',
            field=models.TextField(blank=True, null=True),
        ),
    ]
