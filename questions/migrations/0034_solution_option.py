# Generated by Django 3.2.5 on 2021-12-13 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0033_merge_0024_auto_20211022_2217_0032_auto_20211022_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='option',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Solution', to='questions.option'),
        ),
    ]
