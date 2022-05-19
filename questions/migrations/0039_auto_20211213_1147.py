# Generated by Django 3.2.5 on 2021-12-13 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0038_solution_option'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptionNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='solution',
            name='option',
        ),
        migrations.AddField(
            model_name='solution',
            name='option',
            field=models.ManyToManyField(blank=True, related_name='Solution', to='questions.OptionNumber'),
        ),
    ]