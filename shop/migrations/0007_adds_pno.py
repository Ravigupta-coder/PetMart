# Generated by Django 3.2.9 on 2022-05-09 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20220503_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='adds',
            name='pno',
            field=models.CharField(default='', max_length=12),
        ),
    ]
