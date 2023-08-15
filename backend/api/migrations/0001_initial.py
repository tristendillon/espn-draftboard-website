# Generated by Django 4.2.4 on 2023-08-15 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Draft',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('teams', models.IntegerField()),
                ('roster_spots', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minutes', models.IntegerField(default=0)),
                ('seconds', models.IntegerField(default=0)),
                ('draft_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.draft')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('team_image', models.CharField(blank=True, max_length=400)),
                ('draft_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.draft')),
            ],
        ),
        migrations.CreateModel(
            name='Pick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('icon', models.CharField(max_length=400)),
                ('football_team', models.TextField(max_length=50, null=True)),
                ('pick_round', models.IntegerField()),
                ('pick_number', models.IntegerField()),
                ('position', models.CharField(max_length=10)),
                ('draft_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.draft')),
            ],
        ),
    ]
