# Generated by Django 3.1.4 on 2020-12-29 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myliterature', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='literature',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
