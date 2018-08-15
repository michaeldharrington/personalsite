# Generated by Django 2.0.7 on 2018-08-07 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0010_auto_20180807_0206'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='projectimages',
            name='project',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='right_text',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='project',
            name='code',
        ),
        migrations.RemoveField(
            model_name='project',
            name='highlighted',
        ),
        migrations.RemoveField(
            model_name='project',
            name='language',
        ),
        migrations.RemoveField(
            model_name='project',
            name='left_images',
        ),
        migrations.RemoveField(
            model_name='project',
            name='left_text',
        ),
        migrations.RemoveField(
            model_name='project',
            name='linenos',
        ),
        migrations.RemoveField(
            model_name='project',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='project',
            name='right_images',
        ),
        migrations.RemoveField(
            model_name='project',
            name='style',
        ),
        migrations.DeleteModel(
            name='ProjectImages',
        ),
        migrations.AddField(
            model_name='projectimage',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='public.Project'),
        ),
    ]