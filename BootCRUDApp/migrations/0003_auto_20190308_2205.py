# Generated by Django 2.0.6 on 2019-03-08 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BootCRUDApp', '0002_garbagesellmodel_foreignkeytouser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='garbagesellmodel',
            old_name='name',
            new_name='Name',
        ),
    ]