# Generated by Django 3.2.5 on 2021-07-11 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0018_auto_20210711_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='question',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='solution', to='questions.question'),
        ),
    ]