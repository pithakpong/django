# Generated by Django 4.1.6 on 2023-02-08 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namning_app', '0003_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
