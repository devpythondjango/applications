# Generated by Django 4.2.5 on 2023-09-20 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_remove_username_group_remove_username_hemisid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='username',
            name='javob',
            field=models.TextField(blank=True, null=True),
        ),
    ]