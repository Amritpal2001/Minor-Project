# Generated by Django 3.2.4 on 2021-07-03 08:57

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0014_alter_question_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=tinymce.models.HTMLField(),
        ),
    ]