# Generated by Django 4.2.4 on 2023-08-15 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_team_team_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='team_image',
        ),
    ]
