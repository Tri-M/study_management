# Generated by Django 3.1.12 on 2024-11-20 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='study',
            old_name='study_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='study',
            old_name='sponsor_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='study',
            old_name='study_name',
            new_name='sponsor',
        ),
        migrations.RemoveField(
            model_name='study',
            name='study_phase',
        ),
        migrations.AddField(
            model_name='study',
            name='phase',
            field=models.CharField(default='Phase I', max_length=255),
        ),
    ]
