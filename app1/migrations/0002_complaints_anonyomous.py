# Generated by Django 4.2.2 on 2023-08-27 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='anonyomous',
            field=models.BooleanField(default=False),
        ),
    ]
