# Generated by Django 3.2.5 on 2021-07-12 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0004_auto_20210707_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='desc',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Description'),
        ),
    ]
