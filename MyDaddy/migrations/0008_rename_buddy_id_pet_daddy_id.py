# Generated by Django 4.0 on 2022-02-06 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyDaddy', '0007_daddy_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='buddy_id',
            new_name='daddy_id',
        ),
    ]
