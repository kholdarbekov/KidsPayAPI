# Generated by Django 2.2.6 on 2019-11-10 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191109_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('deleted', 'Deleted')], default='active', max_length=12),
        ),
    ]
