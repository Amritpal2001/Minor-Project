# Generated by Django 3.2.4 on 2021-06-28 16:09

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0009_auto_20210623_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=mdeditor.fields.MDTextField(),
        ),
    ]