# Generated by Django 4.2.4 on 2023-08-15 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_team_team_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_image',
            field=models.CharField(default='0'),
        ),
    ]
