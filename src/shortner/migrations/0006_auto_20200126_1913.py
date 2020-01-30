# Generated by Django 3.0.2 on 2020-01-27 00:13

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0005_auto_20200126_1607'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='shorturl',
            managers=[
                ('inactiveObject', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='shorturl',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='shorturl',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]
